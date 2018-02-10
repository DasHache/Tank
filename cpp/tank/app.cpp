#include "app.h"
#include "frame.h"

bool A::OnInit()
{
	Frame* f = Frame::make_frame();
	f->Show(true);
	return true;
}


