import type { Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load = (async ({ locals }) => {
	return { user: locals.user };
}) satisfies PageServerLoad;

export const actions = {
	createItem: async ({ request }) => {
		// Get form data
		const formData = await request.formData();
		console.log('create new item', formData);
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
