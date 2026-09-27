---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underwriting arrangement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: written contract between parties that commits the underwriter to assuming risk
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/UnderwritingArrangement
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: underwriting arrangement
type: Ontology Class
---

# underwriting arrangement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/UnderwritingArrangement>

## Definition

written contract between parties that commits the underwriter to assuming risk

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Underwriter](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md)

## Annotations

- **label**: underwriting arrangement
- **definition**: written contract between parties that commits the underwriter to assuming risk

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
