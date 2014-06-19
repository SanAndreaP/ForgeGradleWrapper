#include "setupForge.h"

//(*InternalHeaders(setupForge)
#include <wx/intl.h>
#include <wx/string.h>
//*)
#include <Python.h>
#include <sstream>
#include <string>

//(*IdInit(setupForge)
const long setupForge::ID_TEXTCTRL1 = wxNewId();
const long setupForge::ID_RICHTEXTCTRL1 = wxNewId();
//*)

BEGIN_EVENT_TABLE(setupForge,wxPanel)
	//(*EventTable(setupForge)
	//*)
END_EVENT_TABLE()

setupForge::setupForge(wxWindow* parent,wxWindowID id,const wxPoint& pos,const wxSize& size)
{
	//(*Initialize(setupForge)
	Create(parent, id, wxDefaultPosition, wxSize(800,600), wxTAB_TRAVERSAL, _T("id"));
	SetBackgroundColour(wxColour(255,192,192));
	TextCtrl1 = new wxTextCtrl(this, ID_TEXTCTRL1, _("Text"), wxPoint(8,8), wxDefaultSize, 0, wxDefaultValidator, _T("ID_TEXTCTRL1"));
	RichTextCtrl1 = new wxRichTextCtrl(this, ID_RICHTEXTCTRL1, _("Text"), wxPoint(8,32), wxSize(512,416), wxRE_MULTILINE, wxDefaultValidator, _T("ID_RICHTEXTCTRL1"));
	wxRichTextAttr rchtxtAttr_1;
	rchtxtAttr_1.SetBulletStyle(wxTEXT_ATTR_BULLET_STYLE_ALIGN_LEFT);
	//*)

    std::stringstream buffer;
    std::streambuf * old = std::cout.rdbuf(buffer.rdbuf());

	Py_Initialize();
    PyRun_SimpleString("import sys; sys.path.append('.')");
    //PyRun_SimpleString("import mytest;");
    PyRun_SimpleString("print \"Hello\"");
    std::string text = buffer.str();
    Py_Finalize();
    this->RichTextCtrl1->AppendText(text);
    std::cout.rdbuf(old);
}

setupForge::~setupForge()
{
	//(*Destroy(setupForge)
	//*)
}

