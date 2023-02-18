# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\google\protobuf\service_reflection.py
# Compiled at: 2011-01-24 07:39:36
# Size of source mod 2**32: 11294 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign2 ::= expr . expr ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
attribute ::= expr . LOAD_ATTR
attribute37 ::= expr . LOAD_METHOD
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr expr CALL_METHOD_3
call ::= expr . expr expr expr expr expr CALL_METHOD_5
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
expr ::= LOAD_CONST . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= expr load_closure . BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_8
lambda_body ::= load_closure LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_8
lambda_body ::= pos_arg . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= expr load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
subscript ::= expr . expr BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testtrue ::= expr . jmp_true
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
__author__ = 'petar@google.com (Petar Petrov)'

class GeneratedServiceType(type):
    _DESCRIPTOR_KEY = 'DESCRIPTOR'

    def __init__(cls, name, bases, dictionary):
        if GeneratedServiceType._DESCRIPTOR_KEY not in dictionary:
            return
        descriptor = dictionary[GeneratedServiceType._DESCRIPTOR_KEY]
        service_builder = _ServiceBuilder(descriptor)
        service_builder.BuildService(cls)


class GeneratedServiceStubType(GeneratedServiceType):
    _DESCRIPTOR_KEY = 'DESCRIPTOR'

    def __init__(cls, name, bases, dictionary):
        super(GeneratedServiceStubType, cls).__init__(name, bases, dictionary)
        if GeneratedServiceStubType._DESCRIPTOR_KEY not in dictionary:
            return
        descriptor = dictionary[GeneratedServiceStubType._DESCRIPTOR_KEY]
        service_stub_builder = _ServiceStubBuilder(descriptor)
        service_stub_builder.BuildServiceStub(cls)


class _ServiceBuilder(object):

    def __init__(self, service_descriptor):
        self.descriptor = service_descriptor

    def BuildService(self, cls):

        def _WrapCallMethod(srvc, method_descriptor, rpc_controller, request, callback):
            return self._CallMethod(srvc, method_descriptor, rpc_controller, request, callback)

        self.cls = cls
        cls.CallMethod = _WrapCallMethod
        cls.GetDescriptor = staticmethod((lambda: self.descriptor))
        cls.GetDescriptor.__doc__ = 'Returns the service descriptor.'
        cls.GetRequestClass = self._GetRequestClass
        cls.GetResponseClass = self._GetResponseClass
        for method in self.descriptor.methods:
            setattr(cls, method.name, self._GenerateNonImplementedMethod(method))

    def _CallMethod(self, srvc, method_descriptor, rpc_controller, request, callback):
        if method_descriptor.containing_service != self.descriptor:
            raise RuntimeError('CallMethod() given method descriptor for wrong service type.')
        method = getattr(srvc, method_descriptor.name)
        return method(rpc_controller, request, callback)

    def _GetRequestClass(self, method_descriptor):
        if method_descriptor.containing_service != self.descriptor:
            raise RuntimeError('GetRequestClass() given method descriptor for wrong service type.')
        return method_descriptor.input_type._concrete_class

    def _GetResponseClass(self, method_descriptor):
        if method_descriptor.containing_service != self.descriptor:
            raise RuntimeError('GetResponseClass() given method descriptor for wrong service type.')
        return method_descriptor.output_type._concrete_class

    def _GenerateNonImplementedMethod(self, method):
        return (lambda inst, rpc_controller, request, callback: self._NonImplementedMethod(method.name, rpc_controller, callback))

    def _NonImplementedMethod(self, method_name, rpc_controller, callback):
        rpc_controller.SetFailed('Method %s not implemented.' % method_name)
        callback(None)


class _ServiceStubBuilder(object):

    def __init__(self, service_descriptor):
        self.descriptor = service_descriptor

    def BuildServiceStub(self, cls):

        def _ServiceStubInit(stub, rpc_channel):
            stub.rpc_channel = rpc_channel

        self.cls = cls
        cls.__init__ = _ServiceStubInit
        for method in self.descriptor.methods:
            setattr(cls, method.name, self._GenerateStubMethod(method))

    def _GenerateStubMethod--- This code section failed: ---

 L. 266         0  LOAD_CONST               (None,)
                2  LOAD_CLOSURE             'method'
                4  LOAD_CLOSURE             'self'
                6  BUILD_TUPLE_2         2 
                8  LOAD_LAMBDA              '<code_object <lambda>>'
               10  LOAD_STR                 '_ServiceStubBuilder._GenerateStubMethod.<locals>.<lambda>'
               12  MAKE_FUNCTION_9          'default, closure'
               14  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `None' instruction at offset -1

    def _StubMethod(self, stub, method_descriptor, rpc_controller, request, callback):
        return stub.rpc_channel.CallMethod(method_descriptor, rpc_controller, request, method_descriptor.output_type._concrete_class, callback)
