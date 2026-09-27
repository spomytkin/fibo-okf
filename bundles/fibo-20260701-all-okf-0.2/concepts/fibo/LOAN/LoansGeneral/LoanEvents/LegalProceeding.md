---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal proceeding
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal step or action taken at the direction of, or by the authority of, a court or agency
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/isAgainst
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LegalProceeding
sources:
- id: fibo-source-48fe43dc99
  resource: references/fibo/LOAN/LoansGeneral/LoanEvents.rdf
  sha256: 48fe43dc99b1d7ca56ee712ff80baad56b5ac6abd1e4cb8ac5342e7bdee88e6e
  title: FIBO source LOAN/LoansGeneral/LoanEvents.rdf
title: legal proceeding
type: Ontology Class
---

# legal proceeding

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LegalProceeding>

## Definition

legal step or action taken at the direction of, or by the authority of, a court or agency

## Relationships

- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Constraints

- **[isAgainst](/concepts/fibo/LOAN/LoansGeneral/LoanEvents/isAgainst.md)**: some values from of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label** (en): legal proceeding
- **definition** (en): legal step or action taken at the direction of, or by the authority of, a court or agency

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
