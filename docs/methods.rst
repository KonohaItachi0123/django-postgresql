Methods on Node and Edge
========================

*Listed below are the methods that are useful for building/manipulating/querying the graph. We ignore here the methods used only for internal functionality.*

Node
^^^^


Manager Methods
"""""""""""""""


**roots(self, node=None)**

Returns a Queryset of all root nodes (nodes with no parents) in the Node model. If a node instance is specified, returns only the roots for that node.

**leaves(self, node=None)**

Returns a Queryset of all leaf nodes (nodes with no children) in the Node model. If a node instance is specified, returns only the leaves for that node.


Model Methods
"""""""""""""

Methods used for building/manipulating
**************************************

**add_child(self, child, \*\*kwargs)**

Provided with a Node instance, attaches that instance as a child to the current Node instance

**remove_child(self, child, delete_node=False)**

Removes the edge connecting this node to the provided child Node instance, and optionally deletes the child node as well

**add_parent(self, parent, \\*args, \*\*kwargs)**

Provided with a Node instance, attaches the current instance as a child to the provided Node instance

**remove_parent(self, parent, delete_node=False)**

Removes the edge connecting this node to parent, and optionally deletes the parent node as well



Methods used for querying
*************************

**ancestors(self, \*\*kwargs)**

Returns a QuerySet of all nodes in connected paths in a rootward direction

**ancestors_count(self)**

Returns an integer number representing the total number of ancestor nodes

**self_and_ancestors(self, \*\*kwargs)**

Returns a QuerySet of all nodes in connected paths in a rootward direction, prepending with self

**ancestors_and_self(self, \*\*kwargs)**

Returns a QuerySet of all nodes in connected paths in a rootward direction, appending with self

**descendants(self, \*\*kwargs)**

Returns a QuerySet of all nodes in connected paths in a leafward direction

**descendants_count(self)**

Returns an integer number representing the total number of descendant nodes

**self_and_descendants(self, \*\*kwargs)**

Returns a QuerySet of all nodes in connected paths in a leafward direction, prepending with self

**descendants_and_self(self, \*\*kwargs)**

Returns a QuerySet of all nodes in connected paths in a leafward direction, appending with self

**clan(self, \*\*kwargs)**

Returns a QuerySet with all ancestors nodes, self, and all descendant nodes

**clan_count(self)**

Returns an integer number representing the total number of clan nodes

**siblings(self)**

Returns a QuerySet of all nodes that share a parent with this node, excluding self

**siblings_count(self)**

Returns count of all nodes that share a parent with this node

**siblings_with_self(self)**

Returns a QuerySet of all nodes that share a parent with this node and self

**partners(self)**

Returns a QuerySet of all nodes that share a child with this node, excluding self

**partners_count(self)**

Returns count of all nodes that share a child with this node

**partners_with_self(self)**

Returns a QuerySet of all nodes that share a child with this node and self

**path_exists(self, ending_node, \*\*kwargs)**

Given an ending Node instance, returns a boolean value determining whether there is a path from the current Node instance to the ending Node instance

Optional keyword argument: directional (boolean: if True, path searching operates normally, in a leafward only direction. If False, search operates in both directions)

**path(self, ending_node, \*\*kwargs)**

Returns a QuerySet of the shortest path from self to ending node, optionally in either direction. The resulting Queryset is sorted from root-side, toward leaf-side, regardless of the relative position of starting and ending nodes.

Optional keyword argument: directional (boolean: if True, path searching operates normally, in a leafward only direction. If False, search operates in both directions)

**distance(self, ending_node, \*\*kwargs)**

Returns the shortest hops count to the target node

**is_root(self)**

Returns True if the current Node instance has children, but no parents

**is_leaf(self)**

Returns True if the current Node instance has parents, but no children

**is_island(self)**

Returns True if the current Node instance has no parents nor children

**is_ancestor_of(self, ending_node, \*\*kwargs)**

Provided an ending_node Node instance, returns True if the current Node instance and is an ancestor of the provided Node instance

Optional keyword argument: directional (boolean: if True, path searching operates normally, in a leafward only direction. If False, search operates in both directions)

**is_descendant_of(self, ending_node, \*\*kwargs)**

Provided an ending_node Node instance, returns True if the current Node instance and is a descendant of the provided Node instance

Optional keyword argument: directional (boolean: if True, path searching operates normally, in a leafward only direction. If False, search operates in both directions)

**is_sibling_of(self, ending_node)**

Provided an ending_node Node instance, returns True if the provided Node instance and the current Node instance share a parent Node

**is_partner_of(self, ending_node)**

Provided an ending_node Node instance, returns True if the provided Node instance and the current Node instance share a child Node

**node_depth(self)**

Returns an integer representing the depth of this Node instance from furthest root

*Not yet implemented*

**connected_graph(self, \*\*kwargs)**

Returns a QuerySet of all nodes connected in any way to the current Node instance

**descendants_tree(self)**

Returns a tree-like structure with descendants for the current Node

**ancestors_tree(self)**

Returns a tree-like structure with ancestors for the current Node

**roots(self)**

Returns a QuerySet of all root nodes, if any, for the current Node

**leaves(self)**

Returns a QuerySet of all leaf nodes, if any, for the current Node

**descendants_edges(self)**

Returns a QuerySet of descendant Edge instances for the current Node

**ancestors_edges(self)**

Returns a QuerySet of ancestor Edge instances for the current Node

**clan_edges(self)**

Returns a QuerySet of all Edge instances associated with a given node





Edge
^^^^


Manager Methods
"""""""""""""""


**from_nodes_queryset(self, nodes_queryset)**

Provided a QuerySet of nodes, returns a QuerySet of all Edge instances where a parent and child Node are within the QuerySet of nodes

**descendants(self, node, \*\*kwargs)**

Returns a QuerySet of all Edge instances descended from the given Node instance

**ancestors(self, node, \*\*kwargs)**

Returns a QuerySet of all Edge instances which are ancestors of the given Node instance

**clan(self, node, \*\*kwargs)**

Returns a QuerySet of all Edge instances for ancestors, self, and descendants

**path(self, start_node, end_node, \*\*kwargs)**

Returns a QuerySet of all Edge instances for the shortest path from start_node to end_node

**validate_route(self, edges, \*\*kwargs)**

Given a list or set of Edge instances, verify that they result in a contiguous route

*Not yet implemented.*

**sort(self, edges, \*\*kwargs)**

Given a list or set of Edge instances, sort them from root-side to leaf-side

*Not yet implemented.*

**insert_node(self, edge, node, clone_to_rootside=False, clone_to_leafside=False, pre_save=None, post_save=None)**

Inserts a node into an existing Edge instance. Returns a tuple of the newly created rootside_edge (parent to the inserted node) and leafside_edge (child to the inserted node).

Process:

1. Add a new Edge from the parent Node of the current Edge instance to the provided Node instance, optionally cloning properties of the existing Edge.
2. Add a new Edge from the provided Node instance to the child Node of the current Edge instance, optionally cloning properties of the existing Edge.
3. Remove the original Edge instance.

The instance will still exist in memory, though not in database (https://docs.djangoproject.com/en/3.1/ref/models/instances/#refreshing-objects-from-database). Recommend running the following after conducting the deletion:
    del instancename

Cloning will fail if a field has unique=True, so a pre_save function can be passed into this method. Likewise, a post_save function can be passed in to rebuild relationships. For instance, if you have a `name` field that is unique and generated automatically in the model's save() method, you could pass in a the following `pre_save` function to clear the name prior to saving the new Edge instance(s):

::

    def pre_save(new_edge):
        new_edge.name = ""
        return new_edge

A more complete example, where we have models named NetworkEdge & NetworkNode, and we want to insert a new Node (n2) into Edge e1, while copying e1's field properties (except `name`) to the newly created rootside Edge instance (n1 to n2) is shown below.

::

    Original        Final

    n1  o           n1  o
        |                 \
        |                  o n2
        |                 /
    n3  o           n3  o


::

    from myapp.models import NetworkEdge, NetworkNode

    n1 = NetworkNode.objects.create(name="n1")
    n2 = NetworkNode.objects.create(name="n2")
    n3 = NetworkNode.objects.create(name="n3")

    # Connect n3 to n1
    n1.add_child(n3)

    e1 = NetworkEdge.objects.last()

    # function to clear the `name` field, which is autogenerated and must be unique
    def pre_save(new_edge):
        new_edge.name = ""
        return new_edge

    NetworkEdge.objects.insert_node(e1, n2, clone_to_rootside=True, pre_save=pre_save)
