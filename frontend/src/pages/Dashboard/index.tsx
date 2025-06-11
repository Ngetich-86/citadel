import DashboardLayout from "@/components/dashboard/DashboardLayout";


export default function DashboardHome() {
  return (
    <DashboardLayout>
      <h1 className="text-2xl font-bold mb-4">Welcome to Citadel Dashboard</h1>
      <p>Inventory stats and quick actions here.</p>
    </DashboardLayout>
  );
}