from distutils.core import setup
setup(
  name = 'farm_compiler',
  packages = ['farm_compiler'], # this must be the same as the name above
  version = '1.0.1',
  description = 'A compiler for the Farm programming language',
  long_description='''
  The Farm Compiler is written in python and has three main functions:
  def compile_string(string): ~Takes a python string of Farm commands and compiles it.
  def compile_file(name): ~Compiles a text file, or any file with farm_compiler commands in it.
  def write_to_file(string, name): ~Takes a python string, compiles it, and writes the
  resulting farm_compiler result to the name specified.''',
  author = 'Joshua Weinstein',
  author_email = 'jweinst1@berkeley.edu',
  url = 'https://github.com/jweinst1/Farm_Compiler', # use the URL to the github repo
  download_url = 'https://github.com/Timoeller/Farm_Compiler/archive/1.0.1.tar.gz', # I'll explain this in a second
  keywords = ['compilers', 'programming', 'farm_compiler', 'farm'], # arbitrary keywords
  classifiers = [],
)

