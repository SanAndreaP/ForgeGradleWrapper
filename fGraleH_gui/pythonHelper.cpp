#include "pythonHelper.hpp"

namespace pythonHelper {
    std::string getStringFromTuple(boost::python::tuple tupleObj, int index) {
        boost::python::str pyStr = boost::python::extract<boost::python::str>(tupleObj[index]);
        const char *cStr = boost::python::extract<const char *>(pyStr);
        return std::string(cStr);
    }

    std::string addFuncReference(std::string funcName, std::function<void(std::string, void*)> funcRef, void* ptr) {
        std::pair<std::function<void(std::string, void*)>, void*> func = std::pair<std::function<void(std::string, void*)>, void*>(funcRef, ptr);
        m_funcCalls.insert(std::pair<std::string, std::pair<std::function<void(std::string, void*)>, void*>>(funcName, func));
        return std::string("StdoutCatcher('") + funcName + std::string("')");
    }

    void initRedirection() {
        Py_InitModule("redirection", RedirectionMethods);
        PyRun_SimpleString("\
import redirection\n\
class StdoutCatcher:\n\
    def __init__(self, type):\n\
        self._type = type\n\
    def write(self, stuff):\n\
        redirection.stdoeredirect(stuff, self._type)");
    }
}
