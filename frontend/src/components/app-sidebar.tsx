import { Sidebar, SidebarContent, SidebarGroup, SidebarGroupContent, SidebarGroupLabel, SidebarMenu, SidebarMenuItem, SidebarMenuButton, SidebarHeader, useSidebar } from "@/components/ui/sidebar"
import { Link, useLocation } from 'react-router-dom'
import { PanelLeftOpen, PanelLeftClose, LayoutDashboard } from "lucide-react"
import { Button } from "@/components/ui/button";

const items = [
    {
        title: "Dashboard",
        path: "/",
        icon: LayoutDashboard,
    }
]

export function AppSidebar() 
{
    const location = useLocation();
    const { open, toggleSidebar } = useSidebar();

    return (
        <Sidebar collapsible="icon">
            <SidebarHeader>
                <div className="flex justify-between items-center">
                    { open && 
                        <span className="text-2xl text-orange-500 font-semibold">
                            NozzleUI
                        </span>
                    }
                    
                    <Button variant="ghost" onClick={() => toggleSidebar()} className={open ? "" : "w-full"}>
                        { open && <PanelLeftClose className="text-gray-800" /> }
                        { !open && <PanelLeftOpen className="text-gray-800" /> }
                    </Button>
                </div>
            </SidebarHeader>
            
            <SidebarContent>
                <SidebarGroup>
                    <SidebarGroupLabel>
                        Pages
                    </SidebarGroupLabel>
                    <SidebarGroupContent>
                        <SidebarMenu>
                            {items.map((item) => (
                                <SidebarMenuItem key={item.title}>
                                    <SidebarMenuButton asChild isActive={location.pathname === item.path}>
                                        <Link to={item.path}>
                                            <item.icon />
                                            <span>{item.title}</span>
                                        </Link>
                                    </SidebarMenuButton>
                                </SidebarMenuItem>
                            ))}
                        </SidebarMenu>
                    </SidebarGroupContent>
                </SidebarGroup>
            </SidebarContent>
        </Sidebar>
    )
}