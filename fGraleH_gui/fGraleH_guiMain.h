/***************************************************************
 * Name:      fGraleH_guiMain.h
 * Purpose:   Defines Application Frame
 * Author:    SanAndreasP ()
 * Created:   2014-06-18
 * Copyright: SanAndreasP ()
 * License:
 **************************************************************/

#ifndef FGRALEH_GUIMAIN_H
#define FGRALEH_GUIMAIN_H

//(*Headers(fGraleH_guiFrame)
#include <wx/panel.h>
#include <wx/bmpbuttn.h>
#include <wx/frame.h>
//*)
#include "setupForge.h"
//#include "mainMenu.h"

class fGraleH_guiFrame: public wxFrame
{
    public:
        enum Panels {MAIN_MENU, STP_FORGE};
        fGraleH_guiFrame(wxWindow* parent,wxWindowID id = -1);
        virtual ~fGraleH_guiFrame();
        void changePanel(Panels panel);

    private:

        //(*Handlers(fGraleH_guiFrame)
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        void OnResize(wxSizeEvent& event);
        void OnBBtn_SetupForgeClick(wxCommandEvent& event);
        //*)

        //(*Identifiers(fGraleH_guiFrame)
        static const long ID_BITMAPBUTTON2;
        static const long ID_BITMAPBUTTON1;
        static const long ID_PANEL1;
        //*)

        //(*Declarations(fGraleH_guiFrame)
        wxPanel* P_Main;
        wxBitmapButton* BitmapButton1;
        wxBitmapButton* BBtn_SetupForge;
        //*)

        DECLARE_EVENT_TABLE()

        wxPanel *P_SetupForge;
};

#endif // FGRALEH_GUIMAIN_H
