/***************************************************************
 * Name:      fGraleH_guiApp.cpp
 * Purpose:   Code for Application Class
 * Author:    SanAndreasP ()
 * Created:   2014-06-18
 * Copyright: SanAndreasP ()
 * License:
 **************************************************************/

#include "fGraleH_guiApp.h"

//(*AppHeaders
#include "fGraleH_guiMain.h"
#include <wx/image.h>
//*)

IMPLEMENT_APP(fGraleH_guiApp);

bool fGraleH_guiApp::OnInit()
{
    //(*AppInitialize
    bool wxsOK = true;
    wxInitAllImageHandlers();
    if ( wxsOK )
    {
    	fGraleH_guiFrame* Frame = new fGraleH_guiFrame(0);
    	Frame->Show();
    	SetTopWindow(Frame);
    }
    //*)
    return wxsOK;

}
