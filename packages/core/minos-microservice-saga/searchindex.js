Search.setIndex({docnames:["api/minos","api/minos.saga","api/minos.saga.context","api/minos.saga.definitions","api/minos.saga.definitions.operations","api/minos.saga.definitions.saga","api/minos.saga.definitions.steps","api/minos.saga.definitions.steps.abc","api/minos.saga.definitions.steps.conditional","api/minos.saga.definitions.steps.local","api/minos.saga.definitions.steps.remote","api/minos.saga.definitions.types","api/minos.saga.exceptions","api/minos.saga.executions","api/minos.saga.executions.commit","api/minos.saga.executions.executors","api/minos.saga.executions.executors.abc","api/minos.saga.executions.executors.local","api/minos.saga.executions.executors.request","api/minos.saga.executions.executors.response","api/minos.saga.executions.saga","api/minos.saga.executions.status","api/minos.saga.executions.steps","api/minos.saga.executions.steps.abc","api/minos.saga.executions.steps.conditional","api/minos.saga.executions.steps.local","api/minos.saga.executions.steps.remote","api/minos.saga.executions.storage","api/minos.saga.manager","api/minos.saga.messages","api/minos.saga.middleware","api/minos.saga.services","api/minos.saga.utils","authors","history","index","readme","runthetests","usage"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":5,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,"sphinx.ext.viewcode":1,sphinx:56},filenames:["api/minos.rst","api/minos.saga.rst","api/minos.saga.context.rst","api/minos.saga.definitions.rst","api/minos.saga.definitions.operations.rst","api/minos.saga.definitions.saga.rst","api/minos.saga.definitions.steps.rst","api/minos.saga.definitions.steps.abc.rst","api/minos.saga.definitions.steps.conditional.rst","api/minos.saga.definitions.steps.local.rst","api/minos.saga.definitions.steps.remote.rst","api/minos.saga.definitions.types.rst","api/minos.saga.exceptions.rst","api/minos.saga.executions.rst","api/minos.saga.executions.commit.rst","api/minos.saga.executions.executors.rst","api/minos.saga.executions.executors.abc.rst","api/minos.saga.executions.executors.local.rst","api/minos.saga.executions.executors.request.rst","api/minos.saga.executions.executors.response.rst","api/minos.saga.executions.saga.rst","api/minos.saga.executions.status.rst","api/minos.saga.executions.steps.rst","api/minos.saga.executions.steps.abc.rst","api/minos.saga.executions.steps.conditional.rst","api/minos.saga.executions.steps.local.rst","api/minos.saga.executions.steps.remote.rst","api/minos.saga.executions.storage.rst","api/minos.saga.manager.rst","api/minos.saga.messages.rst","api/minos.saga.middleware.rst","api/minos.saga.services.rst","api/minos.saga.utils.rst","authors.rst","history.rst","index.rst","readme.rst","runthetests.rst","usage.rst"],objects:{"":[[0,0,0,"-","minos"]],"minos.saga":[[2,0,0,"-","context"],[3,0,0,"-","definitions"],[12,0,0,"-","exceptions"],[13,0,0,"-","executions"],[28,0,0,"-","manager"],[29,0,0,"-","messages"],[30,0,0,"-","middleware"],[31,0,0,"-","services"],[32,0,0,"-","utils"]],"minos.saga.context":[[2,1,1,"","SagaContext"]],"minos.saga.context.SagaContext":[[2,2,1,"","__init__"],[2,3,1,"","avro_bytes"],[2,3,1,"","avro_data"],[2,4,1,"","avro_schema"],[2,3,1,"","avro_str"],[2,4,1,"","classname"],[2,2,1,"","clear"],[2,2,1,"","decode_data"],[2,2,1,"","decode_schema"],[2,2,1,"","empty"],[2,2,1,"","encode_data"],[2,2,1,"","encode_schema"],[2,3,1,"","fields"],[2,2,1,"","from_avro"],[2,2,1,"","from_avro_bytes"],[2,2,1,"","from_avro_str"],[2,2,1,"","from_model_type"],[2,2,1,"","from_typed_dict"],[2,2,1,"","get"],[2,2,1,"","items"],[2,2,1,"","keys"],[2,4,1,"","model_type"],[2,2,1,"","pop"],[2,2,1,"","popitem"],[2,2,1,"","setdefault"],[2,2,1,"","to_avro_bytes"],[2,2,1,"","to_avro_str"],[2,4,1,"","type_hints"],[2,4,1,"","type_hints_parameters"],[2,2,1,"","update"],[2,2,1,"","values"]],"minos.saga.definitions":[[4,0,0,"-","operations"],[5,0,0,"-","saga"],[6,0,0,"-","steps"],[11,0,0,"-","types"]],"minos.saga.definitions.operations":[[4,1,1,"","SagaOperation"]],"minos.saga.definitions.operations.SagaOperation":[[4,2,1,"","__init__"],[4,2,1,"","from_raw"],[4,3,1,"","parameterized"],[4,3,1,"","raw"]],"minos.saga.definitions.saga":[[5,1,1,"","Saga"]],"minos.saga.definitions.saga.Saga":[[5,2,1,"","__init__"],[5,2,1,"","commit"],[5,2,1,"","conditional_step"],[5,2,1,"","from_raw"],[5,2,1,"","local_step"],[5,3,1,"","raw"],[5,2,1,"","remote_step"],[5,2,1,"","step"],[5,2,1,"","validate"]],"minos.saga.definitions.steps":[[7,0,0,"-","abc"],[8,0,0,"-","conditional"],[9,0,0,"-","local"],[10,0,0,"-","remote"]],"minos.saga.definitions.steps.abc":[[7,1,1,"","SagaStep"]],"minos.saga.definitions.steps.abc.SagaStep":[[7,2,1,"","__init__"],[7,2,1,"","commit"],[7,2,1,"","conditional_step"],[7,2,1,"","from_raw"],[7,2,1,"","local_step"],[7,3,1,"","raw"],[7,2,1,"","remote_step"],[7,2,1,"","step"],[7,2,1,"","validate"]],"minos.saga.definitions.steps.conditional":[[8,1,1,"","ConditionalSagaStep"],[8,1,1,"","ElseThenAlternative"],[8,1,1,"","IfThenAlternative"]],"minos.saga.definitions.steps.conditional.ConditionalSagaStep":[[8,2,1,"","__init__"],[8,2,1,"","commit"],[8,2,1,"","conditional_step"],[8,2,1,"","else_then"],[8,4,1,"","else_then_alternative"],[8,2,1,"","from_raw"],[8,2,1,"","if_then"],[8,4,1,"","if_then_alternatives"],[8,2,1,"","local_step"],[8,3,1,"","raw"],[8,2,1,"","remote_step"],[8,2,1,"","step"],[8,2,1,"","validate"]],"minos.saga.definitions.steps.conditional.ElseThenAlternative":[[8,2,1,"","__init__"],[8,2,1,"","from_raw"],[8,3,1,"","raw"],[8,2,1,"","validate"]],"minos.saga.definitions.steps.conditional.IfThenAlternative":[[8,2,1,"","__init__"],[8,2,1,"","from_raw"],[8,3,1,"","raw"],[8,2,1,"","validate"]],"minos.saga.definitions.steps.local":[[9,1,1,"","LocalSagaStep"]],"minos.saga.definitions.steps.local.LocalSagaStep":[[9,2,1,"","__init__"],[9,2,1,"","commit"],[9,2,1,"","conditional_step"],[9,2,1,"","from_raw"],[9,2,1,"","local_step"],[9,2,1,"","on_execute"],[9,2,1,"","on_failure"],[9,3,1,"","raw"],[9,2,1,"","remote_step"],[9,2,1,"","step"],[9,2,1,"","validate"]],"minos.saga.definitions.steps.remote":[[10,1,1,"","RemoteSagaStep"]],"minos.saga.definitions.steps.remote.RemoteSagaStep":[[10,2,1,"","__init__"],[10,2,1,"","commit"],[10,2,1,"","conditional_step"],[10,2,1,"","from_raw"],[10,2,1,"","local_step"],[10,2,1,"","on_error"],[10,2,1,"","on_execute"],[10,2,1,"","on_failure"],[10,2,1,"","on_success"],[10,3,1,"","raw"],[10,2,1,"","remote_step"],[10,2,1,"","step"],[10,2,1,"","validate"]],"minos.saga.exceptions":[[12,5,1,"","AlreadyCommittedException"],[12,5,1,"","AlreadyOnSagaException"],[12,5,1,"","EmptySagaException"],[12,5,1,"","EmptySagaStepException"],[12,5,1,"","ExecutorException"],[12,5,1,"","MultipleElseThenException"],[12,5,1,"","MultipleOnErrorException"],[12,5,1,"","MultipleOnExecuteException"],[12,5,1,"","MultipleOnFailureException"],[12,5,1,"","MultipleOnSuccessException"],[12,5,1,"","SagaException"],[12,5,1,"","SagaExecutionAlreadyExecutedException"],[12,5,1,"","SagaExecutionException"],[12,5,1,"","SagaExecutionNotFoundException"],[12,5,1,"","SagaFailedCommitCallbackException"],[12,5,1,"","SagaFailedExecutionException"],[12,5,1,"","SagaFailedExecutionStepException"],[12,5,1,"","SagaNotCommittedException"],[12,5,1,"","SagaNotDefinedException"],[12,5,1,"","SagaPausedExecutionStepException"],[12,5,1,"","SagaResponseException"],[12,5,1,"","SagaRollbackExecutionException"],[12,5,1,"","SagaRollbackExecutionStepException"],[12,5,1,"","SagaStepException"],[12,5,1,"","SagaStepExecutionException"],[12,5,1,"","UndefinedOnExecuteException"]],"minos.saga.exceptions.AlreadyCommittedException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.AlreadyOnSagaException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.EmptySagaException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.EmptySagaStepException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.ExecutorException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.MultipleElseThenException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.MultipleOnErrorException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.MultipleOnExecuteException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.MultipleOnFailureException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.MultipleOnSuccessException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaExecutionAlreadyExecutedException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaExecutionException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaExecutionNotFoundException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaFailedCommitCallbackException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaFailedExecutionException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaFailedExecutionStepException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaNotCommittedException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaNotDefinedException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaPausedExecutionStepException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaResponseException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaRollbackExecutionException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaRollbackExecutionStepException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaStepException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.SagaStepExecutionException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.exceptions.UndefinedOnExecuteException":[[12,2,1,"","__init__"],[12,4,1,"","args"],[12,2,1,"","with_traceback"]],"minos.saga.executions":[[14,0,0,"-","commit"],[15,0,0,"-","executors"],[20,0,0,"-","saga"],[21,0,0,"-","status"],[22,0,0,"-","steps"],[27,0,0,"-","storage"]],"minos.saga.executions.commit":[[14,1,1,"","TransactionCommitter"]],"minos.saga.executions.commit.TransactionCommitter":[[14,2,1,"","__init__"],[14,2,1,"","commit"],[14,2,1,"","reject"],[14,4,1,"","transactions"]],"minos.saga.executions.executors":[[16,0,0,"-","abc"],[17,0,0,"-","local"],[18,0,0,"-","request"],[19,0,0,"-","response"]],"minos.saga.executions.executors.abc":[[16,1,1,"","Executor"]],"minos.saga.executions.executors.abc.Executor":[[16,2,1,"","__init__"],[16,2,1,"","exec"],[16,2,1,"","exec_function"]],"minos.saga.executions.executors.local":[[17,1,1,"","LocalExecutor"]],"minos.saga.executions.executors.local.LocalExecutor":[[17,2,1,"","__init__"],[17,2,1,"","exec"],[17,2,1,"","exec_function"]],"minos.saga.executions.executors.request":[[18,1,1,"","RequestExecutor"]],"minos.saga.executions.executors.request.RequestExecutor":[[18,2,1,"","__init__"],[18,2,1,"","exec"],[18,2,1,"","exec_function"]],"minos.saga.executions.executors.response":[[19,1,1,"","ResponseExecutor"]],"minos.saga.executions.executors.response.ResponseExecutor":[[19,2,1,"","__init__"],[19,2,1,"","exec"],[19,2,1,"","exec_function"]],"minos.saga.executions.saga":[[20,1,1,"","SagaExecution"]],"minos.saga.executions.saga.SagaExecution":[[20,2,1,"","__init__"],[20,2,1,"","commit"],[20,2,1,"","execute"],[20,2,1,"","from_definition"],[20,2,1,"","from_raw"],[20,2,1,"","from_saga"],[20,3,1,"","raw"],[20,2,1,"","reject"],[20,2,1,"","rollback"]],"minos.saga.executions.status":[[21,1,1,"","SagaStatus"],[21,1,1,"","SagaStepStatus"]],"minos.saga.executions.status.SagaStatus":[[21,4,1,"","Created"],[21,4,1,"","Errored"],[21,4,1,"","Finished"],[21,4,1,"","Paused"],[21,4,1,"","Running"],[21,2,1,"","from_raw"],[21,3,1,"","raw"]],"minos.saga.executions.status.SagaStepStatus":[[21,4,1,"","Created"],[21,4,1,"","ErroredByOnExecute"],[21,4,1,"","ErroredOnError"],[21,4,1,"","ErroredOnExecute"],[21,4,1,"","ErroredOnFailure"],[21,4,1,"","ErroredOnSuccess"],[21,4,1,"","Finished"],[21,4,1,"","FinishedOnExecute"],[21,4,1,"","PausedByOnExecute"],[21,4,1,"","PausedOnFailure"],[21,4,1,"","RunningOnError"],[21,4,1,"","RunningOnExecute"],[21,4,1,"","RunningOnFailure"],[21,4,1,"","RunningOnSuccess"],[21,2,1,"","from_raw"],[21,3,1,"","raw"]],"minos.saga.executions.steps":[[23,0,0,"-","abc"],[24,0,0,"-","conditional"],[25,0,0,"-","local"],[26,0,0,"-","remote"]],"minos.saga.executions.steps.abc":[[23,1,1,"","SagaStepExecution"]],"minos.saga.executions.steps.abc.SagaStepExecution":[[23,2,1,"","__init__"],[23,2,1,"","execute"],[23,2,1,"","from_definition"],[23,2,1,"","from_raw"],[23,3,1,"","raw"],[23,2,1,"","rollback"]],"minos.saga.executions.steps.conditional":[[24,1,1,"","ConditionalSagaStepExecution"]],"minos.saga.executions.steps.conditional.ConditionalSagaStepExecution":[[24,2,1,"","__init__"],[24,4,1,"","definition"],[24,2,1,"","execute"],[24,2,1,"","from_definition"],[24,2,1,"","from_raw"],[24,4,1,"","inner"],[24,3,1,"","raw"],[24,2,1,"","rollback"]],"minos.saga.executions.steps.local":[[25,1,1,"","LocalSagaStepExecution"]],"minos.saga.executions.steps.local.LocalSagaStepExecution":[[25,2,1,"","__init__"],[25,4,1,"","definition"],[25,2,1,"","execute"],[25,2,1,"","from_definition"],[25,2,1,"","from_raw"],[25,3,1,"","raw"],[25,2,1,"","rollback"]],"minos.saga.executions.steps.remote":[[26,1,1,"","RemoteSagaStepExecution"]],"minos.saga.executions.steps.remote.RemoteSagaStepExecution":[[26,2,1,"","__init__"],[26,4,1,"","definition"],[26,2,1,"","execute"],[26,2,1,"","from_definition"],[26,2,1,"","from_raw"],[26,3,1,"","raw"],[26,2,1,"","rollback"]],"minos.saga.executions.storage":[[27,1,1,"","SagaExecutionStorage"]],"minos.saga.executions.storage.SagaExecutionStorage":[[27,2,1,"","__init__"],[27,2,1,"","delete"],[27,2,1,"","from_config"],[27,2,1,"","load"],[27,2,1,"","store"]],"minos.saga.messages":[[29,1,1,"","SagaRequest"],[29,1,1,"","SagaResponse"],[29,1,1,"","SagaResponseStatus"]],"minos.saga.messages.SagaRequest":[[29,2,1,"","__init__"],[29,2,1,"","content"],[29,3,1,"","target"]],"minos.saga.messages.SagaResponse":[[29,2,1,"","__init__"],[29,2,1,"","content"],[29,2,1,"","from_message"],[29,3,1,"","ok"],[29,3,1,"","related_services"],[29,3,1,"","status"],[29,3,1,"","uuid"]],"minos.saga.messages.SagaResponseStatus":[[29,4,1,"","ERROR"],[29,4,1,"","SUCCESS"],[29,4,1,"","SYSTEM_ERROR"],[29,2,1,"","from_raw"]],"minos.saga.middleware":[[30,6,1,"","transactional_command"]],"minos.saga.services":[[31,1,1,"","SagaService"]],"minos.saga.services.SagaService":[[31,2,1,"","__init__"]],"minos.saga.utils":[[32,6,1,"","get_service_name"]],minos:[[1,0,0,"-","saga"]]},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","property","Python property"],"4":["py","attribute","Python attribute"],"5":["py","exception","Python exception"],"6":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:property","4":"py:attribute","5":"py:exception","6":"py:function"},terms:{"0":35,"01":35,"02":35,"03":35,"04":35,"05":35,"06":35,"07":35,"08":35,"09":35,"1":35,"10":35,"11":35,"12":35,"14":35,"15":35,"17":35,"19":35,"2":[2,35],"20":35,"200":29,"2021":35,"2022":35,"23":35,"26":35,"27":35,"28":35,"3":35,"30":35,"31":35,"4":35,"400":29,"4141ae73":2,"48ad":2,"5":35,"500":29,"6":35,"7":35,"8":35,"8153":2,"9":35,"abstract":[7,23],"byte":2,"case":2,"class":[2,4,5,7,8,9,10,14,16,17,18,19,20,21,23,24,25,26,27,29,31,34],"default":[2,34],"enum":[21,29],"function":[9,10,16,17,18,19,30,34],"import":38,"int":29,"new":[2,4,5,7,8,9,10,20,21,23,24,25,26,27,29,34],"return":[2,4,5,7,8,9,10,12,14,16,17,18,19,20,21,23,24,25,26,27,29,30,32,34],"static":[2,23,24,25,26],"true":[2,4,20,29,34],"try":12,"while":12,A:[2,4,5,7,8,9,10,14,18,20,21,23,24,25,26,27,29],Be:34,For:36,If:[2,5,8,20],In:[2,36,37],On:[9,10],The:[2,5,8,9,10,16,17,18,19,20,21,23,24,25,26,27,29,30,36],Then:8,To:38,__init__:[2,4,5,7,8,9,10,12,14,16,17,18,19,20,23,24,25,26,27,29,31],__traceback__:12,abc:[2,3,5,6,8,9,10,13,15,17,18,19,22,24,25,26,27,29,30],accessor:34,action:34,actual:[17,19],ad:[5,34],add:[5,8,34],addit:[2,4,5,7,8,9,10,14,16,17,18,19,20,23,24,25,26,27,29,34,36],advantag:34,aggreg:34,alberto:33,alia:2,all:2,allow:34,alonso:33,alreadi:12,already_rollback:[20,23,25,26],alreadycommittedexcept:12,alreadyonsagaexcept:12,also:[2,34],altern:[8,12],amigo:33,among:5,amount:34,an:[2,5,7,8,9,10,12,17,18,19,20,26,27,29,36],andrea:33,ani:[2,4,5,7,8,9,10,16,17,18,19,20,23,24,25,26,29,34],anoth:12,anyth:[5,7,8,9,10,14,20,27],api:[34,36],approach:34,ar:[4,12],architectur:36,arg:[2,5,7,8,9,10,12,16,17,18,19,20,23,24,25,26,29,31],argument:[2,4,5,7,8,9,10,14,16,17,18,19,20,23,24,25,26,27,34],async:[14,16,17,18,19,20,23,24,25,26,29,30],asynchron:36,attribut:34,autocommit:[20,34],automat:20,autoreject:[20,34],avail:36,avro:2,avro_byt:2,avro_data:2,avro_schema:2,avro_str:2,await:[5,8,9,10,17,18,19,30],base:[2,4,5,7,8,9,10,12,14,16,17,18,19,20,21,23,24,25,26,27,29,31],batch_mod:2,behaviour:34,best:36,between:34,block:34,bool:[2,4,8,20,29,34],bound:[2,4],broker:[18,29,34],broker_pool:14,broker_publish:[14,18],brokermessag:29,bucket:2,bucketmodel:2,bug:34,bugfix:34,build:[2,4,5,7,8,9,10,20,21,23,24,25,26,27,29],call:[8,9,10,34],callabl:[4,5,8,9,10,16,17,18,19,30],callback:[4,5,9,10,12,18,34],can:34,cannot:12,cd:37,chang:34,channel:36,check:[5,7,8,9,10,29],clariteia:33,classmethod:[2,4,5,7,8,9,10,20,21,23,24,25,26,27,29],classnam:2,clear:2,code:[29,35],collect:[2,5,9,10,17,18,19,30],com:33,come:30,command:[18,26,30,34],commandrepli:34,commandstatu:12,commit:[1,5,7,8,9,10,12,13,17,20,34,36],commitexecutor:34,committ:14,common:[2,12,27,34],compat:34,compens:34,compensatori:20,complet:34,compos:37,comput:[2,20,21,23,24,25,26],concurr:34,condit:[3,5,6,7,9,10,13,22,34],conditional_step:[5,7,8,9,10],conditionalsagastep:[5,7,8,9,10,24,34],conditionalsagastepexecut:[24,34],config:[27,32,34],constructor:[2,34],consum:[20,26],contain:[2,19,29,30,34],content:[18,19,29],context:[0,1,5,8,9,10,17,18,19,20,23,24,25,26],contextvar:34,contributor:33,core:33,correspond:[2,18],cqr:36,creat:[2,5,7,8,9,10,20,21,23,25,26,34,36],credit:33,current:[2,7,8,9,10],d:[2,37],data:[2,30],datadecod:2,dataencod:2,datatransferobject:2,db_name:27,decod:2,decode_data:2,decode_schema:2,defin:[5,12,34],definit:[0,1,16,17,18,19,20,23,24,25,26,34],delet:[27,34],depend:[34,37],deprec:[5,34],dev:33,develop:[33,35],dict:[2,4,5,7,8,9,10,20,23,24,25,26,34],dictionari:2,directli:34,directori:37,discuss:35,disk:34,distribut:36,docker:37,document:34,doe:[2,5,7,8,9,10,14,20,27],driven:36,dto:2,dure:[14,23,24,26],dynam:[2,34],dynamichandl:34,dynamichandlerpool:34,dynamicmodel:2,e8a72aeec0b5:2,e:2,ee4a:2,either:2,els:[2,8,12],else_then:[8,34],else_then_altern:8,elsethenaltern:8,empti:[2,12,20,34],emptysagaexcept:12,emptysagastepexcept:12,encod:2,encode_data:2,encode_schema:2,engin:37,enrich:34,environ:36,error:[10,12,21,29,34],error_messag:12,erroredbyonexecut:21,erroredonerror:21,erroredonexecut:21,erroredonfailur:21,erroredonsuccess:21,event:36,everywher:34,except:[0,1,5,7,8,9,10,19,34],exec:[12,16,17,18,19],exec_funct:[16,17,18,19],execut:[0,1,2,5,8,9,10,12,29,30,34],executed_step:14,execution_uuid:[14,16,17,19],executor:[1,12,13,34],executorexcept:12,expos:34,extend:34,f:2,fail:[12,34],failur:[9,10,12,21],fals:[2,4,5,20,23,25,26,34],favor:34,fenchak:33,field:[2,34],file:34,finish:21,finishedonexecut:21,first:[14,33,34],fix:34,flag:34,follow:2,found:[2,12],framework:36,from:[2,4,5,7,8,9,10,20,21,23,24,25,26,27,29,30,34,38],from_avro:2,from_avro_byt:2,from_avro_str:2,from_config:27,from_definit:[20,23,24,25,26],from_messag:29,from_model_typ:2,from_raw:[4,5,7,8,9,10,20,21,23,24,25,26,29,34],from_saga:20,from_typed_dict:2,fulfil:36,func:[16,17,18,19],garcia:33,gener:[2,4,5,7,9,10,18,20,29,30],get:[2,8,14,29,32,35],get_service_nam:32,getitem:34,getter:[2,4],github:36,gitter:36,given:[2,8,16,27],go:36,ha:[2,9,10,18],handl:[30,34],have:37,header:34,heir:34,help:35,helper:34,hierarchi:34,histori:35,host:36,identifi:[14,20,27,29],if_then:8,if_then_altern:8,ifthenaltern:8,immedi:20,implement:34,improv:34,index:[2,35],initi:20,inject:34,injector:34,inner:[24,30],instal:37,instanc:[2,4,5,7,8,9,10,17,18,19,20,21,23,24,25,26,27,29,34],instead:34,integr:34,intenum:29,intern:36,introduct:35,invoke_particip:34,issu:36,item:[2,34],iter:2,json:27,k:2,keep:2,kei:[2,27],keyerror:2,kwarg:[2,4,5,7,8,9,10,14,16,17,18,19,20,23,24,25,26,27,29,31],lack:2,latest:34,launch:34,lead:33,leverag:36,librari:37,licens:35,like:2,limit:34,list:[2,8,14],lmdb:27,load:27,local:[3,5,6,7,8,10,13,15,22,34],local_step:[5,7,8,9,10,34],localexecutor:[17,34],localsagastep:[5,7,8,9,10,25,34],localsagastepexecut:[25,34],localst:27,logic:[18,34],make:37,manag:[0,1,34],manual:20,map:[2,9,10],md:34,memori:34,messag:[0,1,5,10,12,18,19,20,26,34,36],met:8,metadata:34,method:[2,5,7,8,9,10,12,14,18,20,26,27,34],microservic:[5,14,29,34,38],middlewar:[0,1,34],mino:[34,38],minor:34,minosexcept:12,minosjsonbinaryprotocol:27,minosstoragelmdb:27,mit:36,model:[2,29],model_typ:2,modeltyp:2,modifi:12,modul:[0,1,3,6,13,15,22,34,35],most:36,move:[34,37],mucci:33,multipl:12,multipleelsethenexcept:12,multipleonerrorexcept:12,multipleonexecuteexcept:12,multipleonfailureexcept:12,multipleonsuccessexcept:12,must:[8,20,29],mutablemap:2,name:[2,4,5,7,8,9,10,14,16,17,18,19,20,23,24,25,26,27,29,32,34],namespac:[2,35],network:[29,30,34],next:20,none:[2,4,5,7,8,9,10,12,14,17,20,23,24,25,26,27,29,33],noreturn:34,now:34,object:[2,5,8,14,16,20,27,29,31],offici:36,ok:29,okai:29,on_error:[10,34],on_execut:[9,10,34],on_failur:[9,10,34],on_repli:34,on_success:[10,26,34],one:[5,14,20],ones:34,onreplyexecutor:34,oper:[1,3,5,16,17,18,19,20],option:[2,4,5,9,10,17,18,19,20,24,26,30,34],orchestr:34,order:37,otherwis:[2,4,20],over:36,packag:0,page:[35,36],pair:2,param:2,paramet:[2,4,5,7,8,9,10,14,16,17,18,19,20,21,23,24,25,26,27,29,30],parameter:4,part:34,pass:[2,9,10,34],paus:[12,21,34],pause_on_disk:34,paused_step:20,pausedbyonexecut:21,pausedonfailur:21,perform:[12,18,20,34],place:36,pleas:37,poetri:34,pop:2,popitem:2,posit:[2,7,8,9,10,16,17,18,19,20,23,24,25,26],prado:33,pre:[2,18],present:2,prioriti:[9,10],process:[2,20,34],project:[36,38],propag:34,properti:[2,4,5,7,8,9,10,20,21,23,24,25,26,29],protocol:27,provid:[2,4,5,20,34],publicli:36,publish:18,publishexecutor:34,purpos:[2,5],python:36,question:36,queue:18,rais:[2,5,7,8,9,10,12],raise_on_error:34,raw:[2,4,5,7,8,9,10,20,21,23,24,25,26,29],reactiv:36,readi:5,readm:34,receiv:29,record:2,refer:[9,10,27,36],reject:[14,20,34],relat:[34,36],related_servic:[23,25,26,29],releas:34,remot:[3,5,6,7,8,9,13,22,34],remote_step:[5,7,8,9,10],remotesagastep:[5,7,8,9,10,26],remotesagastepexecut:26,remotestep:34,remov:[2,34],renam:34,replac:34,repli:34,repositori:36,represent:[2,4,5,7,8,9,10,20,21,23,24,25,26,29],request:[13,15,29,30],requestexecutor:[18,34],respect:34,respons:[13,15,16,18,20,26,29,30,34],responseexecutor:[19,34],responsestatu:29,result:[16,17,18,19],return_execut:34,revert:[20,23,24,26],rew:4,rollback:[12,20,23,24,25,26,34],rtype:2,run:[12,18,21,34,35],runningonerror:21,runningonexecut:21,runningonfailur:21,runningonsuccess:21,s:[2,18,34],saga:[0,34,38],saga_manag:31,sagacontext:[2,5,8,9,10,17,18,19,20,23,24,25,26,34],sagaexcept:[12,34],sagaexecut:[20,24,27,34],sagaexecutionalreadyexecutedexcept:12,sagaexecutionexcept:12,sagaexecutionnotfoundexcept:12,sagaexecutionstorag:27,sagafailedcommitcallbackexcept:12,sagafailedexecutionexcept:12,sagafailedexecutionstepexcept:12,sagamanag:34,saganotcommittedexcept:12,saganotdefinedexcept:12,sagaoper:[4,5,16,17,18,19,34],sagapausedexecutionstepexcept:12,sagarequest:[5,10,18,29,34],sagarespons:[10,19,20,26,29,34],sagaresponseexcept:12,sagaresponsestatu:29,sagarollbackexecutionexcept:12,sagarollbackexecutionstepexcept:12,sagaservic:[31,34],sagastatu:[20,21],sagastep:[5,7,8,9,10,23,24,25,26,34],sagastepexcept:12,sagastepexecut:[23,24,25,26,34],sagastepexecutionexcept:12,sagastepoper:4,sagastepstatu:[21,23,25,26],same:8,satisfi:8,schema:2,schemadecod:2,schemaencod:2,scope:34,search:35,second:14,self:[9,10,12],sequenc:[2,5],sergio:33,serial:2,servic:[0,1,32,37],service_nam:34,set:[2,8,9,10,12,29],setdefault:2,setitem:34,setup:34,simpl:34,simplifi:34,singl:2,some:[2,12],sourc:[2,4,5,7,8,9,10,12,14,16,17,18,19,20,21,23,24,25,26,27,29,30,31,32,35],specif:34,specifi:2,stackoverflow:36,state:2,statu:[1,13,20,23,25,26,29],step:[1,3,4,5,12,13,20,21,34],stop:34,storag:[1,13],storage_cl:27,store:[27,34],str:[2,4,5,7,8,9,10,20,21,23,24,25,26,27,29,32,34],string:[2,29],structur:2,sub:34,submodul:0,subpackag:35,success:[10,12,21,29],summari:35,support:34,sure:37,system_error:29,t:[2,4],take:[34,36],target:[2,29],tb:12,test:35,them:34,thi:[2,5,7,8,9,10,14,18,20,27,36],through:34,to_avro_byt:2,to_avro_str:2,transact:[14,20,34],transaction:[30,34],transactional_command:[30,34],transactioncommit:34,transactioncommitt:[14,34],troubl:34,tupl:[2,14],type:[1,2,3,4,5,7,8,9,10,14,16,17,18,19,20,21,23,24,25,26,27,29,30,32,34],type_:2,type_hint:2,type_hints_paramet:2,typed_dict:2,typeddict:2,typedict:2,typevar:[2,4],undefinedonexecuteexcept:12,under:36,union:[2,4,5,7,8,9,10,17,18,19,20,21,23,24,25,26,27],up:37,updat:[2,17,19,20,23,24,26,34],us:[12,14,23,24,26,34,38],usag:[35,36],user:[18,20,34],util:[0,1],uuid:[20,27,29,34],v:2,valid:[5,7,8,9,10],valu:[2,8,14,21,29],variabl:34,view:2,vladyslav:33,wa:14,when:12,which:[14,34,36],why:33,with_compens:34,with_traceback:12,within:34,workflow:34,yet:33,you:[36,37]},titles:["minos namespace","minos.saga package","minos.saga.context module","minos.saga.definitions package","minos.saga.definitions.operations module","minos.saga.definitions.saga module","minos.saga.definitions.steps package","minos.saga.definitions.steps.abc module","minos.saga.definitions.steps.conditional module","minos.saga.definitions.steps.local module","minos.saga.definitions.steps.remote module","minos.saga.definitions.types module","minos.saga.exceptions module","minos.saga.executions package","minos.saga.executions.commit module","minos.saga.executions.executors package","minos.saga.executions.executors.abc module","minos.saga.executions.executors.local module","minos.saga.executions.executors.request module","minos.saga.executions.executors.response module","minos.saga.executions.saga module","minos.saga.executions.status module","minos.saga.executions.steps package","minos.saga.executions.steps.abc module","minos.saga.executions.steps.conditional module","minos.saga.executions.steps.local module","minos.saga.executions.steps.remote module","minos.saga.executions.storage module","minos.saga.manager module","minos.saga.messages module","minos.saga.middleware module","minos.saga.services module","minos.saga.utils module","&lt;no title&gt;","History","Welcome to Minos Microservice Saga\u2019s documentation!","Introduction","Run the tests","Usage"],titleterms:{"0":34,"01":34,"02":34,"03":34,"04":34,"05":34,"06":34,"07":34,"08":34,"09":34,"1":34,"10":34,"11":34,"12":34,"14":34,"15":34,"17":34,"19":34,"2":34,"20":34,"2021":34,"2022":34,"23":34,"26":34,"27":34,"28":34,"3":34,"30":34,"31":34,"4":34,"5":34,"6":34,"7":34,"8":34,"9":34,abc:[7,16,23],code:36,commit:14,condit:[8,24],context:2,definit:[3,4,5,6,7,8,9,10,11],develop:36,discuss:36,document:[35,36],except:12,execut:[13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],executor:[15,16,17,18,19],get:36,help:36,histori:34,indic:35,introduct:36,licens:36,local:[9,17,25],manag:28,messag:29,microservic:[35,36],middlewar:30,mino:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,36],modul:[2,4,5,7,8,9,10,11,12,14,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32],namespac:0,oper:4,packag:[1,3,6,13,15,22],remot:[10,26],request:18,respons:19,run:37,s:35,saga:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,36],servic:31,sourc:36,statu:21,step:[6,7,8,9,10,22,23,24,25,26],storag:27,submodul:[1,3,6,13,15,22],subpackag:[0,1,3,13],summari:36,tabl:35,test:37,type:11,usag:38,util:32,welcom:35}})