#include "listobject.h"
#include "object.h"
void print_python_list_info(PyObject *p)
{
	int k, l;

	l = PyList_Size(p)
	for (k = 0 ; k < l ; k++)
		printf("[*] Size of the Python List = %d", l);
}
