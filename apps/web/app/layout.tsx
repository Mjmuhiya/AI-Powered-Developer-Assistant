import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "CodePilot Workspace",
  description: "AI-powered developer workspace for code understanding, review and testing",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
