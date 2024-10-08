import type { PageServerLoad } from './$types';

export const load = (async ({ fetch }) => {
	const res = await fetch('http://backend:8000/api/health');
	const data = await res.json();
	return { message: data };
}) satisfies PageServerLoad;
