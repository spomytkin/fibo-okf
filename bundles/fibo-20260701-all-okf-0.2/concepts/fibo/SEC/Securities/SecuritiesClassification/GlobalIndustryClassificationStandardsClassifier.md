---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Global Industry Classification Standards classifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: four-tiered standardized classification or delineation for an organization based on the principal business activity
      of the organization
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: GICS classifier
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: GICS code
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/GlobalIndustryClassificationStandardsScheme
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/GlobalIndustryClassificationStandardsClassifier
sources:
- id: fibo-source-6fed3fa3dd
  resource: references/fibo/SEC/Securities/SecuritiesClassification.rdf
  sha256: 6fed3fa3ddd850e875bf020fa5eb79e1d90023fb74888e9c1856e32882bc8f76
  title: FIBO source SEC/Securities/SecuritiesClassification.rdf
title: Global Industry Classification Standards classifier
type: Ontology Class
---

# Global Industry Classification Standards classifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/GlobalIndustryClassificationStandardsClassifier>

## Definition

four-tiered standardized classification or delineation for an organization based on the principal business activity of the organization

## Relationships

- **Subclass of**: [IndustrySectorClassifier](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/GlobalIndustryClassificationStandardsScheme`

## Annotations

- **label**: Global Industry Classification Standards classifier
- **definition**: four-tiered standardized classification or delineation for an organization based on the principal business activity of the organization
- **abbreviation**: GICS classifier
- **abbreviation**: GICS code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
