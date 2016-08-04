/*hello.c*/
#include <stdio.h>
#include "/usr/include/python2.7/Python.h"

int main( int argc, char* argv[])
{
    //
   setenv("PYTHONPATH",".",1);

   PyObject *pName, *pModule, *pDict, *pFunc, *pValue, *presult;


   // Initialize the Python Interpreter
   Py_Initialize();


   // Build the name object
   pName = PyString_FromString((char*)"pla");

   // Load the module object
   pModule = PyImport_Import(pName);


   // pDict is a borrowed reference 
   pDict = PyModule_GetDict(pModule);


   // pFunc is also a borrowed reference 
   // set PLA perceptron weight
   pFunc = PyDict_GetItemString(pDict, (char*)"set_weight");

   if (PyCallable_Check(pFunc))
   {
       pValue=Py_BuildValue("(z)",(char*)"FILE.INI");
       PyErr_Print();
       presult=PyObject_CallObject(pFunc,pValue);
       PyErr_Print();
   } else 
   {
       PyErr_Print();
   }
   printf("(1)Result is %d\n",PyInt_AsLong(presult));
   Py_DECREF(pValue);

   // try PLA predict function
   pFunc = PyDict_GetItemString(pDict, (char*)"predict");

   if (PyCallable_Check(pFunc))
   {
       pValue=Py_BuildValue("(z)",(char*)"5,2");
       PyErr_Print();
       presult=PyObject_CallObject(pFunc,pValue);
       PyErr_Print();
   } else
   {
       PyErr_Print();
   }
   printf("(2)Result is %d\n",PyInt_AsLong(presult));
   Py_DECREF(pValue);
// Clean up
   Py_DECREF(pModule);
   Py_DECREF(pName);

   // Finish the Python Interpreter
   Py_Finalize();    return 0;
}
