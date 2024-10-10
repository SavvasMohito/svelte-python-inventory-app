import type { PageServerLoad } from './$types';

export const load = (async ({ locals, fetch }) => {
	const res = await fetch('http://backend:8000/health');
	const data = await res.json();

	return { message: data, user: locals.user };
}) satisfies PageServerLoad;
