import type { PageServerLoad } from './$types';

export const load = (async ({ fetch, cookies }) => {
	const res = await fetch('http://backend:8000/health');
	const data = await res.json();

	const sessionCookie = cookies.get('session');
	let loggedIn = 'Please log in to view';
	if (sessionCookie) {
		const res2 = await fetch('http://backend:8000/protected', {
			headers: { cookie: sessionCookie }
		});
		if (res2.ok) {
			const data2 = await res2.json();
			loggedIn = data2.message;
		}
	}

	return { message: data, loggedIn: loggedIn };
}) satisfies PageServerLoad;
