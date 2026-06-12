#!/usr/bin/env node

interface ORMInput {
  brand: string;
  reverseSeo: number;
  suppression: number;
  recovery: number;
  brandSerp: number;
  aiVisibility: number;
  reviewSignal: number;
}

interface ORMOutput {
  brand: string;
  reverseSeoScore: number;
  suppressionScore: number;
  recoveryScore: number;
  brandSerpScore: number;
  aiVisibilityScore: number;
  reviewSignalScore: number;
  overallOrmHealth: number;
  prioritySignal: string;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPrioritySignal(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    reverseSeo: "Reverse SEO",
    suppression: "Suppression",
    recovery: "Recovery",
    brandSerp: "Brand SERP",
    aiVisibility: "AI Visibility",
    reviewSignal: "Review Signal",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

export function trackORM(input: ORMInput): ORMOutput {
  const scores = {
    reverseSeo: input.reverseSeo,
    suppression: input.suppression,
    recovery: input.recovery,
    brandSerp: input.brandSerp,
    aiVisibility: input.aiVisibility,
    reviewSignal: input.reviewSignal,
  };
  const overallOrmHealth = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    brand: input.brand,
    reverseSeoScore: input.reverseSeo,
    suppressionScore: input.suppression,
    recoveryScore: input.recovery,
    brandSerpScore: input.brandSerp,
    aiVisibilityScore: input.aiVisibility,
    reviewSignalScore: input.reviewSignal,
    overallOrmHealth,
    prioritySignal: getPrioritySignal(scores),
  };
}

const args = process.argv.slice(2);
const brand = args[0] || "brand-name";
const reverseSeo = parseInt(args[1]) || 45;
const suppression = parseInt(args[2]) || 30;
const recovery = parseInt(args[3]) || 60;
const brandSerp = parseInt(args[4]) || 55;
const aiVisibility = parseInt(args[5]) || 40;
const reviewSignal = parseInt(args[6]) || 70;

const result = trackORM({ brand, reverseSeo, suppression, recovery, brandSerp, aiVisibility, reviewSignal });

console.log(`Brand: ${result.brand}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Reverse SEO Score:     ${result.reverseSeoScore}/100  [${getStatus(result.reverseSeoScore)}]`);
console.log(`Suppression Score:     ${result.suppressionScore}/100  [${getStatus(result.suppressionScore)}]`);
console.log(`Recovery Score:        ${result.recoveryScore}/100  [${getStatus(result.recoveryScore)}]`);
console.log(`Brand SERP Score:      ${result.brandSerpScore}/100  [${getStatus(result.brandSerpScore)}]`);
console.log(`AI Visibility Score:   ${result.aiVisibilityScore}/100  [${getStatus(result.aiVisibilityScore)}]`);
console.log(`Review Signal Score:   ${result.reviewSignalScore}/100  [${getStatus(result.reviewSignalScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall ORM Health:    ${result.overallOrmHealth}/100`);
console.log(`Priority Signal:       ${result.prioritySignal}`);
