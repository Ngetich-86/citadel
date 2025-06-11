export default function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-gray-800 text-white fixed">
      <div className="p-4 font-bold text-xl">Citadel</div>
      <nav className="flex flex-col p-4 space-y-2">
        <a href="/dashboard" className="hover:bg-gray-700 p-2 rounded">Dashboard</a>
        <a href="/dashboard/products" className="hover:bg-gray-700 p-2 rounded">Products</a>
        <a href="/dashboard/orders" className="hover:bg-gray-700 p-2 rounded">Orders</a>
        <a href="/dashboard/settings" className="hover:bg-gray-700 p-2 rounded">Settings</a>
      </nav>
    </aside>
  );
}