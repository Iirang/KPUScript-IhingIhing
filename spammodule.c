#include "Python.h"

static PyObject*

spam_GetRegionNum(PyObject* self, PyObject* Region)
{
	const Py_UNICODE* RegionName = NULL;
	const char* RegionNum = NULL;
	
	if (!PyArg_ParseTuple(Region, "u", &RegionName))
		return NULL;

	if (wcscmp(RegionName, L"서울") == 0)
		RegionNum = "1";
	else if (wcscmp(RegionName, L"제주") == 0)
		RegionNum = "2";
	else if ((wcscmp(RegionName, L"부산") == 0) || wcscmp(RegionName, L"부산경남") == 0)
		RegionNum = "3";
	else
		return NULL;

	return Py_BuildValue("s", RegionNum);
}

static PyMethodDef SpamMethods[] = {
	{"GetRegionNum", spam_GetRegionNum, METH_VARARGS,
	"convert Region name to Region number."},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",
	"It is Ihing-Ihing C module.",
	-1, SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}