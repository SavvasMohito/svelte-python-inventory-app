import { env } from '$env/dynamic/private';
import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	const sessionCookie = event.cookies.get('session');
	if (sessionCookie) {
		const res = await fetch(`${env.BACKEND_URL}/auth/session`, {
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
