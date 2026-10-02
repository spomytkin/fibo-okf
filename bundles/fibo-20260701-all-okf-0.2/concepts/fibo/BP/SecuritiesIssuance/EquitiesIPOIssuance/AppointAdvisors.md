---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: appoint advisors
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/designates
    value: Nd07d6a5051bd4f24a9be9379b6bd0825
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance/InitialPublicOfferingProcessStep.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/InitialPublicOfferingProcessStep
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/AppointAdvisors
sources:
- id: fibo-source-fb4230f5b0
  resource: references/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance.rdf
  sha256: fb4230f5b0812f53d30ce91b5b00a7d962d30b713eb159867935983fd6f7bbe7
  title: FIBO source BP/SecuritiesIssuance/EquitiesIPOIssuance.rdf
title: appoint advisors
type: Ontology Class
---

# appoint advisors

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/AppointAdvisors>

## Relationships

- **Subclass of**: [InitialPublicOfferingProcessStep](/concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance/InitialPublicOfferingProcessStep.md)

## Constraints

- **[designates](<https://www.omg.org/spec/Commons/Organizations/designates>)**: some values from value `Nd07d6a5051bd4f24a9be9379b6bd0825`
- **[playsRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole>)**: some values from of type [Issuer](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)

## Annotations

- **label** (en): appoint advisors

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
