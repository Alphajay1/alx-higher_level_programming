#include "python.h"

/**
 * print_python_string - prints info about python strings
 * @p: A pyobject string object
 *
 * Return: void
 */
void print_python_string(PyObject *p)
{
	long int len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}
	len = ((PyASCIIObject *)(p))->len;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}
