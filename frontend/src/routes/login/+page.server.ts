import { env } from '$env/dynamic/private';
import { fail, redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {};

export const actions = {
	logout: async ({ cookies }) => {
		cookies.delete('session', { path: '/', httpOnly: true, secure: false, sameSite: 'lax' });
		throw redirect(302, '/');
	},

	login: async ({ request, cookies }) => {
		// Get form data
		const formData = await request.formData();
		const username = formData.get('username') as string;
		const password = formData.get('password') as string;

		const res = await fetch(`${env.BACKEND_URL}/auth/login`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				username: username,
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

		// API returns error
		const body = await res.json();
		if (body && body.detail) {
			return fail(400, { error: body.detail });
		}
		return fail(400, { error: 'An error occurred' });
	}
} satisfies Actions;
