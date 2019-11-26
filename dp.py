
###########################################################
# Generic dispatcher implementation

def disp(fn):

	class DispatcherImpl:

		def __init__(self):

			class RegisterImpl:

				def __init__(self, the_type):
					self.the_type = the_type

				def __call__(self, the_function):
					self.outer.spec[self.the_type] = the_function

			self.spec = {}
			self.register = RegisterImpl
			self.register.outer = self
		
		def __call__(self, val):
			for k in self.spec:
				if isinstance(val, k):
					# Found specific implementation
					self.spec[k](val)
					return
			# calling default implementation
			fn(val)
			
	return DispatcherImpl()


###########################################################
# Usage of dispatcher to print by type

@disp
def print_it(o):
	print("Default implementation: %s" % str(o))

@print_it.register(str)
def _(s):
	print("String implementation: %s" % s)

@print_it.register(int)
def _(i):
	print("Int implementation: %d" % i)


###########################################################
# Sample calls

print_it("Hello World")
print_it(17)
print_it( (1, 2, 3) )


