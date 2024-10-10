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
	<title>Login</title>
</svelte:head>

<div class="flex justify-center">
	<Card.Root class="w-full max-w-sm">
		<Card.Header>
			<Card.Title class="text-2xl">Login</Card.Title>
			<Card.Description>Enter your username below to login to your account</Card.Description>
		</Card.Header>
		<Card.Content>
			<form action="?/login" method="POST" use:enhance>
				<div class="grid gap-4">
					<div class="grid gap-2">
						<Label for="username">Username</Label>
						<Input id="username" name="username" type="username" placeholder="johndoe" required />
					</div>
					<div class="grid gap-2">
						<div class="flex items-center">
							<Label for="password">Password</Label>
							<!-- <Button formaction="?/forgotPassword" ="ml-auto inline-block text-sm underline">
								Forgot your password?
							</Button> -->
						</div>
						<Input id="password" name="password" type="password" required />
					</div>
					<Button type="submit" class="w-full">Login</Button>
					{#if form?.error}<Alert.Root variant="destructive" class="text-center font-semibold">
							<Alert.Description>{form?.error}</Alert.Description>
						</Alert.Root>{/if}
				</div>
			</form>
			<div class="mt-4 text-center text-sm">
				Don&apos;t have an account?
				<a href="/register" class="underline">Sign up</a>
			</div>
		</Card.Content>
	</Card.Root>
</div>
