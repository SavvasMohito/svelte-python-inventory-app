import type { Item } from '$lib/types';
import { fail, redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load = (async ({ locals, cookies }) => {
	let items: Item[] = [];
	if (locals.user) {
		const sessionCookie = cookies.get('session');
		if (sessionCookie) {
			const res = await fetch('http://backend:8000/items', {
				headers: {
					cookie: sessionCookie,
					'Content-Type': 'application/json'
				}
			});

			if (res.ok) {
				const data = await res.json();
				items = data;
			}
		}
	}
	return { user: locals.user, items: items };
}) satisfies PageServerLoad;

export const actions = {
	createItem: async ({ request, cookies }) => {
		// Get form data
		const formData = await request.formData();
		const sessionCookie = cookies.get('session');
		if (sessionCookie) {
			const res = await fetch('http://backend:8000/items', {
				method: 'POST',
				headers: {
					cookie: sessionCookie,
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					name: formData.get('name'),
					description: formData.get('description'),
					quantity: formData.get('quantity'),
					date: formData.get('date')
				})
			});

			if (res.ok) return;

			// API returns error
			const body = await res.json();
			if (body && body.detail) {
				return fail(400, { error: body.detail });
			}
			return fail(400, { error: 'An error occurred' });
		}
		return redirect(302, '/login');
	},

	updateItem: async ({ request }) => {
		// Get form data
		const formData = await request.formData();
		console.log('update item', formData);
	},

	deleteItem: async ({ request }) => {
		// Get form data
		const formData = await request.formData();
		console.log('delete item', formData);
	}
} satisfies Actions;
