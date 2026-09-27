---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: in default
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The issuer has failed to pay somthing that they are contractually obliged to pay.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: '(review 7 Oct 09) Does this exist as a term? This is a characteristic of the instrument not the rating. Because
      it''s in default you can expect the rating to drop. Applies to instrument not to debtor. So a company may have 3 bond
      issues and may be defualt on only one. 14 Oct: Degrees of defaults e.g. tranche not paying interest due to losses on
      the underlying portrfolio; tranches being used to pay down more senior tranches.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/MD/TemporalCore/SecurityCreditStatuses/SecurityCreditStatus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityCreditStatuses/SecurityCreditStatus
resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityCreditStatuses/InDefault
sources:
- id: fibo-source-e03c8b200b
  resource: references/fibo/MD/TemporalCore/SecurityCreditStatuses.rdf
  sha256: e03c8b200b6a5c2725a08112c4d0ae2e6d50d0fb9df0b05784ec7b794efce940
  title: FIBO source MD/TemporalCore/SecurityCreditStatuses.rdf
title: in default
type: Ontology Class
---

# in default

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityCreditStatuses/InDefault>

## Definition

The issuer has failed to pay somthing that they are contractually obliged to pay.

## Relationships

- **Subclass of**: [SecurityCreditStatus](/concepts/fibo/MD/TemporalCore/SecurityCreditStatuses/SecurityCreditStatus.md)

## Annotations

- **label** (en): in default
- **definition** (en): The issuer has failed to pay somthing that they are contractually obliged to pay.
- **editorialNote** (en): (review 7 Oct 09) Does this exist as a term? This is a characteristic of the instrument not the rating. Because it's in default you can expect the rating to drop. Applies to instrument not to debtor. So a company may have 3 bond issues and may be defualt on only one. 14 Oct: Degrees of defaults e.g. tranche not paying interest due to losses on the underlying portrfolio; tranches being used to pay down more senior tranches.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
