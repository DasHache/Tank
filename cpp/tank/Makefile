

tank: frame.o app.o
	g++ tank.cpp frame.o app.o -L. -I. `wx-config --cxxflags --libs`


frame: frame.cpp frame.h
	g++ frame.cpp -I. `wx-config --cxxflags --libs` -c


app: app.cpp app.h
	g++ app.cpp -I. `wx-config --cxxflags --libs` -c


clean: 
	rm -f *.o
	rm -f tank
