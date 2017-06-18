#-*- coding: utf-8 -*-
from concrete.factory import (
	UsualUserFactory,
	FuckinUserFactory,
)

def main():
	usual_factory = UsualUserFactory()
	usual1 = usual_factory.create("usual1")
	usual2 = usual_factory.create("usual2")
	usual1.do_action()
	usual2.do_action()

	fuckin_factory = FuckinUserFactory()
	fuckin1 = fuckin_factory.create("fuckin1")
	fuckin2 = fuckin_factory.create("fuckin2")
	fuckin1.do_action()
	fuckin2.do_action()

if __name__ == "__main__":
	main()

