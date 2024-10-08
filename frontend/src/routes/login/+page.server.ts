import { fail, redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {};

export const actions = {
	login: async ({ request, cookies }) => {
		// Get form data
		const formData = await request.formData();
		const email = formData.get('email') as string;
		const password = formData.get('password') as string;

		const res = await fetch('http://backend:8000/api/auth/cookie/login', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			},
			body: new URLSearchParams({
				username: email,
				password: password
			})
		});

		if (res.ok) {
			const sessionCookie = res.headers.get('set-cookie');
			if (sessionCookie) {
				cookies.set('session', sessionCookie.split(';')[0], {
					path: '/',
					httpOnly: true,
					secure: false,
					sameSite: 'lax'
				});
				throw redirect(302, '/');
			}
		}

		const errormsg = await res.json();

		if (errormsg && errormsg.detail) {
			if (errormsg.detail === 'LOGIN_BAD_CREDENTIALS')
				return fail(400, { error: 'The credentials are incorrect' });
			if (errormsg.detail === 'LOGIN_USER_NOT_VERIFIED')
				return fail(400, { error: 'The user has not verified their account' });
		}
		return fail(400, { error: 'An error occurred' });
	}
} satisfies Actions;
