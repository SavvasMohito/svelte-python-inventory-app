import { fail, redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {};

export const actions = {
	register: async ({ request }) => {
		// Get form data
		const formData = await request.formData();
		const email = formData.get('email') as string;
		const password = formData.get('password') as string;

		const res = await fetch('http://backend:8000/api/auth/register', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				email: email,
				password: password
			})
		});

		if (res.ok) {
			throw redirect(302, '/login');
		}

		const errormsg = await res.json();
		if (errormsg && errormsg.detail) {
			if (errormsg.detail === 'REGISTER_USER_ALREADY_EXISTS')
				return fail(400, { error: 'This email address is already registered' });
			if (errormsg.detail.code === 'REGISTER_INVALID_PASSWORD')
				return fail(400, { error: errormsg.detail.reason });
		}
		return fail(400, { error: 'An error occurred' });
	}
} satisfies Actions;
