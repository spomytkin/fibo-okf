---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: maturity equivalent p s a
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Prepayment speed that results in the same average life as that computed for the Collateralized Mortgage Obligation
      (CMO), Asset Backed Securities (ABS) or Mortgage Backed Securities (MBS) using the Maturity Prepay Model.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Detailed parameters to follow, but basically these three PSA terms are differentiated by the fact that they reference
      3 different prepayment models, so each of these will refer to a sub-type of the term "Loan Pool Prepayment Model". For
      now the semantics are defined only in this written definition. Add model variants and terms in a future version.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/MaturityEquivalentPSA
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: maturity equivalent p s a
type: Ontology Class
---

# maturity equivalent p s a

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/MaturityEquivalentPSA>

## Definition

Prepayment speed that results in the same average life as that computed for the Collateralized Mortgage Obligation (CMO), Asset Backed Securities (ABS) or Mortgage Backed Securities (MBS) using the Maturity Prepay Model.

## Relationships

- **Subclass of**: [PrepaymentSpeed](/concepts/fibo/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed.md)

## Annotations

- **label** (en): maturity equivalent p s a
- **definition** (en): Prepayment speed that results in the same average life as that computed for the Collateralized Mortgage Obligation (CMO), Asset Backed Securities (ABS) or Mortgage Backed Securities (MBS) using the Maturity Prepay Model.
- **editorialNote** (en): Detailed parameters to follow, but basically these three PSA terms are differentiated by the fact that they reference 3 different prepayment models, so each of these will refer to a sub-type of the term "Loan Pool Prepayment Model". For now the semantics are defined only in this written definition. Add model variants and terms in a future version.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
