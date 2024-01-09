#include <stdio.h>
#include "/usr/include/python3.4/python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: is a list of object
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int idx = 0, len_list = 0;
	pyListobject *clone = (pyListobject *) p;
	pyobject *item;

	len_list = py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", len_list);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (; idx < len_list; ++idx)
	{
		item = pyList_GET_ITEM(p, idx);
		printf("Element %d: %s\n", idx, item->ob_type->tp_name);
	}
	return;
}
