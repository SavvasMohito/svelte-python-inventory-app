<script lang="ts">
	import DeleteItemDialog from '$lib/components/DeleteItemDialog.svelte';
	import EditItemDialog from '$lib/components/EditItemDialog.svelte';
	import NewItemDialog from '$lib/components/NewItemDialog.svelte';
	import * as Card from '$lib/components/ui/card';
	import * as Table from '$lib/components/ui/table';
	import type { Item } from '$lib/types';

	// type Props = {
	// 	items: [];
	// };

	// const { items = $bindable() }: Props = $props();

	const items: Item[] = [
		{
			id: 1,
			name: 'Screwdriver',
			description: 'This is a small screwdriver, I left it in the garage.',
			quantity: '1',
			date: '2021-10-01'
		},
		{
			id: 2,
			name: 'Hammer',
			description: 'This is the orange hammer I bought from the hardware store across the street.',
			quantity: '1',
			date: '2023-12-01'
		},
		{
			id: 3,
			name: 'Wrench',
			description: 'A new wrench my dad game me for my birthday in 2019.',
			quantity: '1',
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
			<NewItemDialog />
		</div>
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
									<DeleteItemDialog {item} />
								</div>
							</Table.Cell>
						</Table.Row>
					{/each}
				</Table.Body>
			</Table.Root>
		</div>
	</Card.Content>
	<Card.Footer>
		<div class="text-xs text-muted-foreground">
			Showing a total of <strong>{items.length}</strong> items
		</div>
	</Card.Footer>
</Card.Root>
