#include "setupForge.h"

//(*InternalHeaders(setupForge)
#include <wx/settings.h>
#include <wx/font.h>
#include <wx/intl.h>
#include <wx/string.h>
//*)

#include "pythonHelper.hpp"

//(*IdInit(setupForge)
const long setupForge::ID_RICHTEXTCTRL1 = wxNewId();
const long setupForge::ID_PANEL1 = wxNewId();
//*)

BEGIN_EVENT_TABLE(setupForge,wxPanel)
	//(*EventTable(setupForge)
	//*)
END_EVENT_TABLE()

setupForge::setupForge(wxWindow* parent,wxWindowID id,const wxPoint& pos,const wxSize& size)
{
	//(*Initialize(setupForge)
	Create(parent, id, wxDefaultPosition, wxSize(800,600), wxTAB_TRAVERSAL, _T("id"));
	Panel1 = new wxPanel(this, ID_PANEL1, wxPoint(0,0), wxSize(800,600), wxTAB_TRAVERSAL, _T("ID_PANEL1"));
	RichTextCtrl1 = new wxRichTextCtrl(Panel1, ID_RICHTEXTCTRL1, wxEmptyString, wxPoint(0,0), wxSize(512,328), wxRE_MULTILINE|wxRE_READONLY|wxVSCROLL, wxDefaultValidator, _T("ID_RICHTEXTCTRL1"));
	wxRichTextAttr rchtxtAttr_1;
	rchtxtAttr_1.SetBulletStyle(wxTEXT_ATTR_BULLET_STYLE_ALIGN_LEFT);
	wxFont Font_1 = wxSystemSettings::GetFont(wxSYS_ANSI_FIXED_FONT);
	if ( !Font_1.Ok() ) Font_1 = wxSystemSettings::GetFont(wxSYS_DEFAULT_GUI_FONT);
	rchtxtAttr_1.SetFontFaceName(Font_1.GetFaceName());
	rchtxtAttr_1.SetFontSize(Font_1.GetPointSize());
	rchtxtAttr_1.SetFontStyle(Font_1.GetStyle());
	rchtxtAttr_1.SetFontUnderlined(Font_1.GetUnderlined());
	rchtxtAttr_1.SetFontWeight(Font_1.GetWeight());
	RichTextCtrl1->SetBasicStyle(rchtxtAttr_1);
	//*)
//	BitmapButton1->SetBitmapHover(wxBitmap(wxImage(_T("C:\\Stuff\\C++ Projects\\ForgeGradleWrapper\\fGraleH_gui\\button_stpFrg_hvr.png"))));
//	BitmapButton2->SetBitmapHover(wxBitmap(wxImage(_T("C:\\Stuff\\C++ Projects\\ForgeGradleWrapper\\fGraleH_gui\\button_stpFrg_hvr.png"))));
}

setupForge::~setupForge()
{
	//(*Destroy(setupForge)
	//*)
}

void onPyStdOut(std::string str, void* ptr) {
    wxRichTextCtrl *ctrl = static_cast<wxRichTextCtrl*>(ptr);
    ctrl->WriteText(str);
}

void onPyStdErr(std::string str, void* ptr) {
    wxRichTextCtrl *ctrl = static_cast<wxRichTextCtrl*>(ptr);
    ctrl->BeginTextColour(wxColour(255, 0, 0));
    ctrl->BeginBold();
    ctrl->WriteText(str);
    ctrl->EndBold();
    ctrl->EndTextColour();
}

void setupForge::OnBitmapButton1Click(wxCommandEvent& event)
{
    try {
        Py_Initialize();
        PyEval_InitThreads();
        boost::python::object main_module = boost::python::import("__main__");
        boost::python::object main_namespace = main_module.attr("__dict__");

        std::string py_stdout = pythonHelper::addFuncReference("stdout", onPyStdOut, this->RichTextCtrl1);
        std::string py_stderr = pythonHelper::addFuncReference("stderr", onPyStdErr, this->RichTextCtrl1);
        pythonHelper::initRedirection();

        boost::python::exec_statement("import sys", main_namespace, main_namespace);
        boost::python::exec_statement(std::string("sys.stdout = ").append(py_stdout).c_str(), main_namespace, main_namespace);
        boost::python::exec_statement(std::string("sys.stderr = ").append(py_stderr).c_str(), main_namespace, main_namespace);

        for( int i = 0; i < 10; i++ ) {
            boost::python::exec_statement("print('Hello Pythonians!')");
        }
        boost::python::exec_statement("1+a");
    } catch( boost::python::error_already_set const& ) {
        PyErr_Print();
        for( int i = 0; i < 10; i++ ) {
            boost::python::exec_statement("print('Hello Pythonians!')");
        }
    }

    Py_Finalize();
}
