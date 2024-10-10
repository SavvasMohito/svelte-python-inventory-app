import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	const sessionCookie = event.cookies.get('session');
	if (sessionCookie) {
		const res = await fetch('http://backend:8000/auth/session', {
			headers: { cookie: sessionCookie }
		});
		if (res.ok) {
			const userData = await res.json();
			event.locals.user = userData;
		} else {
			event.locals.user = undefined;
		}
	} else {
		event.locals.user = undefined;
	}
	const response = await resolve(event);
	return response;
};
