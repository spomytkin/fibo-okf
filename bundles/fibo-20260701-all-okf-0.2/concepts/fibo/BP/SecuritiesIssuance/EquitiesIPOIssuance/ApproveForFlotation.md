---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: approve for flotation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance/InitialPublicOfferingProcessStep.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/InitialPublicOfferingProcessStep
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/ApproveForFlotation
sources:
- id: fibo-source-fb4230f5b0
  resource: references/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance.rdf
  sha256: fb4230f5b0812f53d30ce91b5b00a7d962d30b713eb159867935983fd6f7bbe7
  title: FIBO source BP/SecuritiesIssuance/EquitiesIPOIssuance.rdf
title: approve for flotation
type: Ontology Class
---

# approve for flotation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/ApproveForFlotation>

## Relationships

- **Subclass of**: [InitialPublicOfferingProcessStep](/concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance/InitialPublicOfferingProcessStep.md)

## Constraints

- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Annotations

- **label** (en): approve for flotation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
