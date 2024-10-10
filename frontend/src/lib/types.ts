export type User =
	| {
			id: number;
			username: string;
	  }
	| undefined;

export type Item = {
	id: number;
	name: string;
	description: string;
	quantity: string;
	date: string;
};
