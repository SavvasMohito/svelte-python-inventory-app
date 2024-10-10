<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import * as Card from '$lib/components/ui/card';
	import * as Table from '$lib/components/ui/table';
	import type { Item } from '$lib/types';
	import Trash2 from 'lucide-svelte/icons/trash-2';
	import EditItemDialog from './EditItemDialog.svelte';

	// type Props = {
	// 	items: [];
	// };

	// const { items = $bindable() }: Props = $props();

	const items: Item[] = [
		{
			id: 1,
			name: 'Screwdriver',
			description: 'This is a small screwdriver, I left it in the garage.',
			quantity: 1,
			date: '2021-10-01'
		},
		{
			id: 2,
			name: 'Hammer',
			description: 'This is the orange hammer I bought from the hardware store across the street.',
			quantity: 1,
			date: '2023-12-01'
		},
		{
			id: 3,
			name: 'Wrench',
			description: 'A new wrench my dad game me for my birthday in 2019.',
			quantity: 1,
			date: '2019-05-01'
		}
	];
</script>

<Card.Root
	class="w-full max-w-screen-xl"
	data-x-chunk-description="A list of products in a table with actions. Each row has an image, name, status, price, total sales, created at and actions."
>
	<Card.Header>
		<div class="flex items-center justify-between">
			<Card.Title class="text-xl">Your Inventory Items</Card.Title>
			<Button>+ Add new item</Button>
		</div>
		<!-- <Card.Description>Manage your products and view their sales performance.</Card.Description> -->
	</Card.Header>
	<Card.Content>
		<div class="rounded-md border">
			<Table.Root>
				<Table.Header>
					<Table.Row>
						<Table.Head>Name</Table.Head>
						<Table.Head>Description</Table.Head>
						<Table.Head class="hidden md:table-cell">Quantity</Table.Head>
						<Table.Head class="hidden md:table-cell">Date</Table.Head>
						<Table.Head>
							<span class="sr-only">Actions</span>
						</Table.Head>
					</Table.Row>
				</Table.Header>
				<Table.Body>
					{#each items as item}
						<Table.Row id={item.id.toString()}>
							<Table.Cell class="font-medium">{item.name}</Table.Cell>
							<Table.Cell>{item.description}</Table.Cell>
							<Table.Cell class="hidden md:table-cell">{item.quantity}</Table.Cell>
							<Table.Cell class="hidden text-nowrap md:table-cell">
								{new Date(item.date).toLocaleDateString('en-GB')}
							</Table.Cell>
							<Table.Cell>
								<div class="flex gap-2">
									<EditItemDialog {item} />
									<Button size="icon">
										<Trash2 class="h-5 w-5" />
										<span class="sr-only">Delete</span>
									</Button>
								</div>
							</Table.Cell>
						</Table.Row>
					{/each}
				</Table.Body>
			</Table.Root>
		</div>
	</Card.Content>
	<!-- <Card.Footer>
		<div class="text-xs text-muted-foreground">
			Showing <strong>1-10</strong> of <strong>32</strong> products
		</div>
	</Card.Footer> -->
</Card.Root>
