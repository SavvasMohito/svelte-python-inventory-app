import { fail, redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {};

export const actions = {
	register: async ({ request }) => {
		// Get form data
		const formData = await request.formData();
		const username = formData.get('username') as string;
		const password = formData.get('password') as string;

		const res = await fetch('http://backend:8000/auth/register', {
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
			throw redirect(302, '/login');
		}

		// API returns error
		const body = await res.json();
		if (body && body.detail) {
			return fail(400, { error: body.detail });
		}
		return fail(400, { error: 'An error occurred' });
	}
} satisfies Actions;
