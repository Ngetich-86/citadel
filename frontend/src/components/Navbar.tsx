'use client';

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
// import { Button } from "./ui/button";   
// import { Menu, X } from "lucide-react";

export function Navbar() {
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="bg-gray-800 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link href="/" className="text-lg font-bold">
          MyApp
        </Link>
        {/* <Button onClick={toggleMenu} className="md:hidden"> */}
          {/* {isOpen ? <X size={24} /> : <Menu size={24} />} */}
        {/* </Button> */}
        <div
          className={`${
            isOpen ? "block" : "hidden"
          } md:flex space-x-4 md:space-x-6`}
        >
          <Link href="/" className={`hover:text-gray-300 ${pathname === '/' ? 'text-gray-300' : ''}`}>
            Home
          </Link>
          <Link href="/about" className={`hover:text-gray-300 ${pathname === '/about' ? 'text-gray-300' : ''}`}>
            About
          </Link>
          <Link href="/contact" className={`hover:text-gray-300 ${pathname === '/contact' ? 'text-gray-300' : ''}`}>
            Contact
          </Link>
        </div>
      </div>
    </nav>
  );
}