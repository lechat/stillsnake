import socket
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/',)

# Create server
server = SimpleXMLRPCServer((socket.gethostbyname(socket.gethostname()), 8000), requestHandler=RequestHandler)
server.register_introspection_functions()

# Here are the Wordpress functions:
# Posts (for posts, pages, and custom post types) - Added in WordPress 3.4
# wp.getPost
# wp.getPosts
# wp.newPost
# wp.editPost
# wp.deletePost
# wp.getPostType
# wp.getPostTypes
# wp.getPostFormats
# wp.getPostStatusList
# Taxonomies (for categories, tags, and custom taxonomies) - Added in WordPress 3.4
# wp.getTaxonomy
# wp.getTaxonomies
# wp.getTerm
# wp.getTerms
# wp.newTerm
# wp.editTerm
# wp.deleteTerm
# Media - Added in WordPress 3.1
# wp.getMediaItem
# wp.getMediaLibrary
# wp.uploadFile
# Comments - Added in WordPress 2.7
# wp.getCommentCount
# wp.getComment
# wp.getComments
# wp.newComment
# wp.editComment
# wp.deleteComment
# wp.getCommentStatusList
# Options - Added in WordPress 2.6
# wp.getOptions
# wp.setOptions
# Users
# wp.getUsersBlogs
# wp.getAuthors

def debug_function(*kwargs):
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])

server.register_function(debug_function, 'wp.getPost')
server.register_function(debug_function, 'wp.getPosts')
server.register_function(debug_function, 'wp.newPost')
server.register_function(debug_function, 'wp.editPost')
server.register_function(debug_function, 'wp.deletePost')
server.register_function(debug_function, 'wp.getPostType')
server.register_function(debug_function, 'wp.getPostTypes')
server.register_function(debug_function, 'wp.getPostFormats')
server.register_function(debug_function, 'wp.getPostStatusList')
server.register_function(debug_function, 'wp.getTaxonomy')
server.register_function(debug_function, 'wp.getTaxonomies')
server.register_function(debug_function, 'wp.getTerm')
server.register_function(debug_function, 'wp.getTerms')
server.register_function(debug_function, 'wp.newTerm')
server.register_function(debug_function, 'wp.editTerm')
server.register_function(debug_function, 'wp.deleteTerm')
server.register_function(debug_function, 'wp.getMediaItem')
server.register_function(debug_function, 'wp.getMediaLibrary')
server.register_function(debug_function, 'wp.uploadFile')
server.register_function(debug_function, 'wp.getCommentCount')
server.register_function(debug_function, 'wp.getComment')
server.register_function(debug_function, 'wp.getComments')
server.register_function(debug_function, 'wp.newComment')
server.register_function(debug_function, 'wp.editComment')
server.register_function(debug_function, 'wp.deleteComment')
server.register_function(debug_function, 'wp.getCommentStatusList')
server.register_function(debug_function, 'wp.getOptions')
server.register_function(debug_function, 'wp.setOptions')
server.register_function(debug_function, 'wp.getUsersBlogs')
server.register_function(debug_function, 'wp.getAuthors')

# Run the server's main loop
server.serve_forever()
