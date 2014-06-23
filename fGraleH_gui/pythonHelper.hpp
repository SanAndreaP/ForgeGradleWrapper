#ifndef PYTHONHELPER_HPP_INCLUDED
#define PYTHONHELPER_HPP_INCLUDED

#include <cmath>
#include <boost/python.hpp>
#include <string>
#include <map>
#include <functional>

namespace pythonHelper {
    std::string getStringFromTuple(boost::python::tuple tupleObj, int index);
    void initRedirection();
    std::string addFuncReference(std::string funcName, std::function<void(std::string, void*)> funcRef, void* ptr);

    static std::map<std::string, std::pair<std::function<void(std::string, void*)>, void*>> m_funcCalls;

    static PyObject* redirection_stdoeredirect(PyObject *self, PyObject *args) {
        const char *outstr;
        const char *type;
        if( !PyArg_ParseTuple(args, "ss", &outstr, &type) ) {
            return NULL;
        }

        if( m_funcCalls.find(std::string(type)) != m_funcCalls.end() ) {
            std::pair<std::function<void(std::string, void*)>, void*> fnc = m_funcCalls.at(std::string(type));
            fnc.first(std::string(outstr), fnc.second);
        }

        Py_INCREF(Py_None);
        return Py_None;
    }

    static PyMethodDef RedirectionMethods[] = {
        {"stdoeredirect", redirection_stdoeredirect, METH_VARARGS, "stdout/stderr redirection helper"}
        ,{NULL, NULL, 0, NULL}
    };
}

#endif // PYTHONHELPER_HPP_INCLUDED
