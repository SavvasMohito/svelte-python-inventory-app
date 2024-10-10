<script lang="ts">
	import { enhance } from '$app/forms';
	import * as Alert from '$lib/components/ui/alert/index.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';

	const { form } = $props();
</script>

<svelte:head>
	<title>Register</title>
</svelte:head>

<div class="flex justify-center">
	<Card.Root class="w-full max-w-sm">
		<Card.Header>
			<Card.Title class="text-xl">Sign Up</Card.Title>
			<Card.Description>Enter your information to create an account</Card.Description>
		</Card.Header>
		<Card.Content>
			<form action="?/register" method="POST" use:enhance>
				<div class="grid gap-4">
					<div class="grid gap-2">
						<Label for="username">Username</Label>
						<Input id="username" name="username" type="username" placeholder="johndoe" required />
					</div>
					<div class="grid gap-2">
						<Label for="password">Password</Label>
						<Input id="password" name="password" type="password" />
					</div>
					<Button type="submit" class="w-full">Create an account</Button>
					{#if form?.error}<Alert.Root variant="destructive" class="text-center font-semibold">
							<Alert.Description>{form?.error}</Alert.Description>
						</Alert.Root>{/if}
				</div>
			</form>
			<div class="mt-4 text-center text-sm">
				Already have an account?
				<a href="/login" class="underline"> Sign in </a>
			</div>
		</Card.Content>
	</Card.Root>
</div>
