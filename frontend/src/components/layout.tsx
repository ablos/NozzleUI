import { SidebarProvider } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"

interface LayoutProps
{
    children: React.ReactNode;
}

export default function Layout({ children }: LayoutProps)
{
    return (
        <SidebarProvider>
            <div className="min-h-screen flex w-full">
                <AppSidebar />
            
                <main className="flex-1 p-2">
                    {children}
                </main>
            </div>
        </SidebarProvider>
    );
}