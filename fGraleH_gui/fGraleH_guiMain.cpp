/***************************************************************
 * Name:      fGraleH_guiMain.cpp
 * Purpose:   Code for Application Frame
 * Author:    SanAndreasP ()
 * Created:   2014-06-18
 * Copyright: SanAndreasP ()
 * License:
 **************************************************************/

#include "fGraleH_guiMain.h"
#include "images/button_stpFrg.hpp"
#include <wx/msgdlg.h>

//(*InternalHeaders(fGraleH_guiFrame)
#include <wx/intl.h>
#include <wx/string.h>
//*)

//helper functions
enum wxbuildinfoformat {
    short_f, long_f };

wxString wxbuildinfo(wxbuildinfoformat format)
{
    wxString wxbuild(wxVERSION_STRING);

    if (format == long_f )
    {
#if defined(__WXMSW__)
        wxbuild << _T("-Windows");
#elif defined(__UNIX__)
        wxbuild << _T("-Linux");
#endif

#if wxUSE_UNICODE
        wxbuild << _T("-Unicode build");
#else
        wxbuild << _T("-ANSI build");
#endif // wxUSE_UNICODE
    }

    return wxbuild;
}

//(*IdInit(fGraleH_guiFrame)
const long fGraleH_guiFrame::ID_BITMAPBUTTON2 = wxNewId();
const long fGraleH_guiFrame::ID_BITMAPBUTTON1 = wxNewId();
const long fGraleH_guiFrame::ID_PANEL1 = wxNewId();
//*)

BEGIN_EVENT_TABLE(fGraleH_guiFrame,wxFrame)
    //(*EventTable(fGraleH_guiFrame)
    //*)
END_EVENT_TABLE()

fGraleH_guiFrame::fGraleH_guiFrame(wxWindow* parent,wxWindowID id)
{
    //(*Initialize(fGraleH_guiFrame)
    Create(parent, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxDEFAULT_DIALOG_STYLE|wxCLOSE_BOX|wxFRAME_SHAPED|wxMINIMIZE_BOX, _T("wxID_ANY"));
    SetClientSize(wxSize(800,600));
    P_Main = new wxPanel(this, ID_PANEL1, wxPoint(0,0), wxSize(800,600), wxTAB_TRAVERSAL, _T("ID_PANEL1"));
    BitmapButton1 = new wxBitmapButton(P_Main, ID_BITMAPBUTTON2, wxNullBitmap, wxPoint(256,160), wxSize(304,29), wxBU_AUTODRAW, wxDefaultValidator, _T("ID_BITMAPBUTTON2"));
    BitmapButton1->Disable();
    BitmapButton1->SetBackgroundColour(wxColour(128,128,192));
    BBtn_SetupForge = new wxBitmapButton(P_Main, ID_BITMAPBUTTON1, wxNullBitmap, wxPoint(256,120), wxSize(304,29), wxBU_AUTODRAW, wxDefaultValidator, _T("ID_BITMAPBUTTON1"));
    BBtn_SetupForge->SetBackgroundColour(wxColour(128,128,192));

    Connect(ID_BITMAPBUTTON2,wxEVT_COMMAND_BUTTON_CLICKED,(wxObjectEventFunction)&fGraleH_guiFrame::OnBBtn_SetupForgeClick);
    Connect(ID_BITMAPBUTTON1,wxEVT_COMMAND_BUTTON_CLICKED,(wxObjectEventFunction)&fGraleH_guiFrame::OnBBtn_SetupForgeClick);
    //*)

//    this->SetClientSize(this->NB_Main->GetSize());
    this->CenterOnScreen();
    this->P_SetupForge = new setupForge(this);

    this->BBtn_SetupForge->SetBitmap(wxBitmap(ButtonSetupForge::getNormal()));
    this->BBtn_SetupForge->SetBitmapFocus(wxBitmap(ButtonSetupForge::getFocus()));
    this->BBtn_SetupForge->SetBitmapHover(wxBitmap(ButtonSetupForge::getHover()));
    this->BBtn_SetupForge->SetBitmapDisabled(wxBitmap(ButtonSetupForge::getDisabled()));
    this->BBtn_SetupForge->SetBitmapPressed(wxBitmap(ButtonSetupForge::getPressed()));

    this->BitmapButton1->SetBitmap(wxBitmap(ButtonSetupForge::getNormal()));
    this->BitmapButton1->SetBitmapFocus(wxBitmap(ButtonSetupForge::getFocus()));
    this->BitmapButton1->SetBitmapHover(wxBitmap(ButtonSetupForge::getHover()));
    this->BitmapButton1->SetBitmapDisabled(wxBitmap(ButtonSetupForge::getDisabled()));
    this->BitmapButton1->SetBitmapPressed(wxBitmap(ButtonSetupForge::getPressed()));

    this->P_Main->Show();
    this->P_SetupForge->Hide();
//    this->changePanel(Panels::MAIN_MENU);

//    this->m_panels.at(Panels::STP_FORGE)->Hide();
}

fGraleH_guiFrame::~fGraleH_guiFrame()
{
    //(*Destroy(fGraleH_guiFrame)
    //*)
}

void fGraleH_guiFrame::OnQuit(wxCommandEvent& event)
{
    Close();
}

void fGraleH_guiFrame::OnAbout(wxCommandEvent& event)
{
    wxString msg = wxbuildinfo(long_f);
    wxMessageBox(msg, _("Welcome to..."));
}


void fGraleH_guiFrame::OnResize(wxSizeEvent& event)
{
    event.Skip();
}

void fGraleH_guiFrame::OnBBtn_SetupForgeClick(wxCommandEvent& event)
{
    this->P_Main->Hide();
    this->P_SetupForge->Show();
}
