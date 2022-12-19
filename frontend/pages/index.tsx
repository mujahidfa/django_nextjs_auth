import { signIn, signOut, useSession } from "next-auth/react";
import Head from "next/head";

export default function Home() {
  const { data: session } = useSession();
  console.log("&&&&&&&&&&&&&&&&&&&&&&&&");
  console.log(session);

  return (
    <>
      <Head>
        <title>Django + NextAuth.js</title>
        <meta
          name="description"
          content="Django + NextAuth.js minimal example."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        {session ? (
          <>
            <h1>Hello, you've logged in!</h1>
            <a
              href="/api/auth/signout"
              onClick={(e) => {
                e.preventDefault();
                signOut();
              }}
            >
              Logout
            </a>
          </>
        ) : (
          <>
            <h1>Access Denied</h1>
            <p>
              <a
                href="/api/auth/signin"
                onClick={(e) => {
                  e.preventDefault();
                  signIn();
                }}
              >
                You must be signed in to view this page
              </a>
            </p>
          </>
        )}
      </main>
    </>
  );
}
