---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund administrator
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: role of the party responsible for managing the operational, accounting, and compliance functions of an investment
      fund
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A fund administrator performs administrative tasks on behalf of an investment fund, including net asset value (NAV)
      calculation, financial reporting, investor servicing, and regulatory compliance. The role supports operational efficiency
      and transparency, enabling fund managers to focus on investment strategy.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundAdministrator
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: fund administrator
type: Ontology Class
---

# fund administrator

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundAdministrator>

## Definition

role of the party responsible for managing the operational, accounting, and compliance functions of an investment fund

## Relationships

- **Subclass of**: [ServiceProvider](<https://www.omg.org/spec/Commons/Organizations/ServiceProvider>)

## Annotations

- **label** (en): fund administrator
- **definition** (en): role of the party responsible for managing the operational, accounting, and compliance functions of an investment fund
- **explanatoryNote** (en): A fund administrator performs administrative tasks on behalf of an investment fund, including net asset value (NAV) calculation, financial reporting, investor servicing, and regulatory compliance. The role supports operational efficiency and transparency, enabling fund managers to focus on investment strategy.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
